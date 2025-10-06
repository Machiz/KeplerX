// Form submission handler
document.getElementById('exoplanetForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // 1. Recolectar datos del formulario
    const formData = new FormData(this);
    let data = Object.fromEntries(formData);

    // 2. Convertir todos los valores a número (float)
    for (let key in data) {
        data[key] = parseFloat(data[key]) || 0;
    }

    try {
        // 3. Enviar al backend FastAPI
        let response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        let result = await response.json();

        // 4. Mostrar resultado en el div #result
        document.getElementById("result").innerHTML = `
            <div class="prediction-box">
                <i class="fa-solid fa-robot"></i> <b>Predicción:</b> ${result.prediction}
            </div>
        `;

        console.log("✅ Prediction response:", result);

    } catch (error) {
        console.error("❌ Error calling API:", error);
        alert("Error enviando datos al backend. Revisa la consola.");
    }
});

// Clear form function
function clearForm() {
    if (confirm('¿Seguro que quieres limpiar todos los campos?')) {
        document.getElementById('exoplanetForm').reset();
        document.getElementById("result").innerHTML = "";
    }
}
