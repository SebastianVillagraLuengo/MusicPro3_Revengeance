var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Obtener o inicializar el carrito desde el almacenamiento local
var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

// Función para guardar el carrito en el almacenamiento local
function saveCartItems() {
  localStorage.setItem('cartItems', JSON.stringify(cartItems));
}

// Función para actualizar la cantidad en el carrito
function updateCartItemQuantity(productId, quantity) {
  var cartItem = cartItems.find(function (item) {
    return item.productId === productId;
  });

  if (cartItem) {
    cartItem.quantity = quantity;
  } else {
    cartItems.push({ productId: productId, quantity: quantity });
  }

  saveCartItems();
}

// Función para obtener la cantidad de un producto en el carrito
function getCartItemQuantity(productId) {
  var cartItem = cartItems.find(function (item) {
    return item.productId === productId;
  });

  return cartItem ? cartItem.quantity : 0;
}

// Función para actualizar la cantidad en la base de datos mediante AJAX
function updateQuantityInDatabase(productId, quantity) {
  var request = new XMLHttpRequest();
  request.open('POST', '/actualizar-cantidad/');
  request.setRequestHeader('Content-Type', 'application/json');
  request.setRequestHeader('X-CSRFToken', csrftoken);
  request.onload = function () {
    // Maneja la respuesta de la petición AJAX si es necesario
    if (request.status === 200) {
      // Actualizar visualmente la cantidad en el botón correspondiente
      var quantityElement = document.querySelector(`.btn-quantity[data-id="${productId}"] + .quantity`);
      quantityElement.textContent = quantity;
      quantityElement.dataset.quantity = quantity; // Actualizar el atributo data-quantity
    }
  };
  request.send(JSON.stringify({
    productId: productId,
    quantity: quantity
  }));
}

// Agrega los controladores de eventos a los botones de suma y resta
document.querySelectorAll('.btn-quantity').forEach(function (button) {
  button.addEventListener('click', function (event) {
    event.preventDefault(); // Evita el comportamiento predeterminado del botón
    var quantityElement = button.parentNode.querySelector('.quantity');
    var subtotalElement = button.parentNode.parentNode.querySelector('.subtotal');
    var productId = button.dataset.id;

    if (button.classList.contains('btn-minus')) {
      // Restar uno a la cantidad
      var quantity = parseInt(quantityElement.textContent);
      var updatedQuantity = quantity - 1;
      if (updatedQuantity < 1) {
        updatedQuantity = 1; // Evita que la cantidad sea menor a 1
      }
      quantityElement.textContent = updatedQuantity;
      quantityElement.dataset.quantity = updatedQuantity; // Actualizar el atributo data-quantity
      updateQuantityInDatabase(productId, updatedQuantity);
      updateCartItemQuantity(productId, updatedQuantity);
    } else if (button.classList.contains('btn-plus')) {
      // Sumar uno a la cantidad
      var quantity = parseInt(quantityElement.textContent);
      var updatedQuantity = quantity + 1;
      quantityElement.textContent = updatedQuantity;
      quantityElement.dataset.quantity = updatedQuantity; // Actualizar el atributo data-quantity
      updateQuantityInDatabase(productId, updatedQuantity);
      updateCartItemQuantity(productId, updatedQuantity);
    }
    subtotalElement.textContent = (parseFloat(quantityElement.textContent) * parseFloat(subtotalElement.dataset.price)).toFixed(2);
    updateTotal();
  });
});

// Función para actualizar el total en tiempo real
function updateTotal() {
  var total = 0;
  document.querySelectorAll('.subtotal').forEach(function (subtotalElement) {
    total += parseFloat(subtotalElement.textContent);
  });
  document.querySelector('.total').textContent = total.toFixed(2);
}

// Cargar las cantidades de los productos desde el carrito
document.querySelectorAll('.btn-quantity').forEach(function (button) {
  var productId = button.dataset.id;
  var quantityElement = button.parentNode.querySelector('.quantity');
  var subtotalElement = button.parentNode.parentNode.querySelector('.subtotal');
  var quantity = getCartItemQuantity(productId);

  quantityElement.textContent = quantity;
  quantityElement.dataset.quantity = quantity;
  subtotalElement.textContent = (parseFloat(quantityElement.textContent) * parseFloat(subtotalElement.dataset.price)).toFixed(2);
});

// Actualizar el total al cargar la página
updateTotal();