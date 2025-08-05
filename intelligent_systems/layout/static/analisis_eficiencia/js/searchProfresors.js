document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("buscar-profesor");
    const resultados = document.getElementById("resultados");
    let debounceTimer; // Variable para almacenar el temporizador del debounce

    // Función para realizar la búsqueda
    const buscarProfesores = (query) => {
        if (query.length === 0) {
            resultados.classList.add("hidden");
            return;
        }

        fetch(`/api/academico/buscar-profesores/?q=${encodeURIComponent(query)}`)
            .then((response) => response.json())
            .then((data) => {
                resultados.innerHTML = ""; // Limpia los resultados anteriores
                if (data.length > 0) {
                    resultados.classList.remove("hidden");
                    data.forEach((profesor) => {
                        const li = document.createElement("li");
                        li.textContent = profesor.nombre; // Muestra el nombre completo
                        li.className = "p-2 hover:bg-indigo-100 cursor-pointer";
                        li.addEventListener("click", () => {
                            input.value = profesor.nombre; // Rellena el input
                            resultados.classList.add("hidden");
                        });
                        resultados.appendChild(li);
                    });
                } else {
                    resultados.classList.add("hidden");
                }
            })
            .catch((error) => {
                console.error("Error al buscar profesores:", error);
            });
    };

    // Evento de entrada con debounce
    input.addEventListener("input", () => {
        clearTimeout(debounceTimer); // Limpia el temporizador anterior
        const query = input.value.trim();

        // Inicia un nuevo temporizador
        debounceTimer = setTimeout(() => {
            buscarProfesores(query); // Llama a la función después del retraso
        }, 1000); 
    });

    // Ocultar la lista si el usuario hace clic fuera del componente
    document.addEventListener("click", (e) => {
        if (!input.contains(e.target) && !resultados.contains(e.target)) {
            resultados.classList.add("hidden");
        }
    });
});