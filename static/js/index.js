document.addEventListener('DOMContentLoaded', () => {
    const scriptTag = document.querySelector('script[data-endpoint]');
    const endpoint = scriptTag.getAttribute('data-endpoint');

    fetch(endpoint) // Ruta de tu API
        .then(response => response.json())
        .then(data => {
            const container = document.querySelector('.producto-container');
            container.innerHTML = ''; // Limpiar el contenedor antes de agregar nuevos productos
            data.forEach(producto => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('hogar');
                
                productDiv.innerHTML = `
                    <img class="imagen" src="/static/uploads/${producto.nombre_imagen}" alt="">
                    <div class="card-hogar">
                        <h1 class="title1">${producto.nombre}</h1>
                        <p>${producto.descripcion}</p>
                        <p>Precio: ${producto.precio}</p>
                        <p>Cantidad: ${producto.cantidad}</p>
                        <button class="ver-mas-btn" data-nombre="${producto.nombre}" data-imagen="/static/uploads/${producto.nombre_imagen}" data-descripcion="${producto.descripcion}" data-precio="${producto.precio}" data-cantidad="${producto.cantidad}">Más información aqui</button>
                    </div>
                `;
                container.appendChild(productDiv);
            });

            // Add event listeners to the buttons
            const buttons = document.querySelectorAll('.ver-mas-btn');
            buttons.forEach(button => {
                button.addEventListener('click', (event) => {
                    const nombre = event.target.getAttribute('data-nombre');
                    const imagen = event.target.getAttribute('data-imagen');
                    const descripcion = event.target.getAttribute('data-descripcion');
                    const precio = event.target.getAttribute('data-precio');
                    const cantidad = event.target.getAttribute('data-cantidad');

                    document.getElementById('modalTitle').innerText = nombre;
                    document.getElementById('modalImage').src = imagen;
                    document.getElementById('modalDescription').innerText = descripcion;
                    document.getElementById('modalPrecio').innerText = `Precio: ${precio}`;
                    document.getElementById('modalCantidad').innerText = `Cantidad: ${cantidad}`;

                    document.getElementById('productModal').style.display = 'block';
                    document.body.classList.add('modal-open'); // Disable background interaction
                });
            });

            // Close the modal
            const modal = document.getElementById('productModal');
            const span = document.getElementsByClassName('close')[0];
            span.onclick = function() {
                modal.style.display = 'none';
                document.body.classList.remove('modal-open'); // Enable background interaction
            }
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = 'none';
                    document.body.classList.remove('modal-open'); // Enable background interaction
                }
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});