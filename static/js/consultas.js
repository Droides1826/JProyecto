document.addEventListener('DOMContentLoaded', () => {
    const scriptTag = document.querySelector('script[data-endpoint]');
    const endpoint = scriptTag.getAttribute('data-endpoint');

    fetch(endpoint) 
        .then(response => response.json())
        .then(data => {
            const container = document.querySelector('.producto-container');
            container.innerHTML = ''; 
            data.forEach(producto => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('consultas');
                
                productDiv.innerHTML = `
                    <div class ="contenedor-img">
                        <img class="imagen" src="/static/uploads/${producto.nombre_imagen}" alt="">
                    </div>
                    <div class="card-hogar">
                        <h1 class="title1">${producto.nombre}</h1>
                        <p>${producto.descripcion}</p>
                        <p>${producto.precio}</p>
                        <a class="ver-mas-btn" href="">Más información aqui</a>
                    </div>
                `;
                container.appendChild(productDiv);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});