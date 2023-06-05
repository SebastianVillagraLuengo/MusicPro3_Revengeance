// Obtener el token CSRF
var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Función para actualizar la cantidad en la base de datos mediante AJAX
function updateQuantityInDatabase(productId, quantity) {
    var request = new XMLHttpRequest();
    request.open('POST', 'actualizar-cantidad/');
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('X-CSRFToken', csrfToken);
    request.onload = function() {
        // Maneja la respuesta de la petición AJAX si es necesario
    };
    request.send(JSON.stringify({
        productId: productId,
        quantity: quantity
    }));
}

// Agrega los controladores de eventos a los botones de suma y resta
document.querySelectorAll('.btn-quantity').forEach(function(button) {
    button.addEventListener('click', function() {
        var quantityElement = button.parentNode.querySelector('.quantity');
        var subtotalElement = button.parentNode.parentNode.querySelector('.subtotal');

        if (button.classList.contains('btn-minus')) {
            // Restar uno a la cantidad
            var quantity = parseInt(quantityElement.getAttribute('data-quantity'));
            var updatedQuantity = quantity - 1;
            if (updatedQuantity < 1) {
                updatedQuantity = 1; // Evita que la cantidad sea menor a 1
            }
            quantityElement.textContent = updatedQuantity;
            button.parentNode.querySelector('.quantity').setAttribute('data-quantity', updatedQuantity);
            updateQuantityInDatabase(button.getAttribute('data-id'), updatedQuantity);
        } else if (button.classList.contains('btn-plus')) {
            // Sumar uno a la cantidad
            var quantity = parseInt(quantityElement.getAttribute('data-quantity'));
            var updatedQuantity = quantity + 1;
            quantityElement.textContent = updatedQuantity;
            button.parentNode.querySelector('.quantity').setAttribute('data-quantity', updatedQuantity);
            updateQuantityInDatabase(button.getAttribute('data-id'), updatedQuantity);
        }
        subtotalElement.textContent = (parseFloat(quantityElement.textContent) * parseFloat(subtotalElement.getAttribute('data-price'))).toFixed(2);
        updateTotal();
    });
});

// Función para actualizar el total en tiempo real
function updateTotal() {
    var subtotals = document.querySelectorAll('.subtotal');
    var total = 0;
    subtotals.forEach(function(subtotal) {
        total += parseFloat(subtotal.textContent);
    });
    document.querySelector('.total').textContent = total.toFixed(2);
}