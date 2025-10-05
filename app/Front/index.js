     // Form submission handler
        document.getElementById('exoplanetForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Collect form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Show success message
            alert('Data submitted successfully to the Exoplanet Research Database!');
            console.log('Submitted data:', data);
            
            // Optionally clear form after submission
            // this.reset();
        });

        // Clear form function
        function clearForm() {
            if (confirm('Are you sure you want to clear all form data?')) {
                document.getElementById('exoplanetForm').reset();
            }
        }

        // Add input validation for numeric fields
        const numericInputs = document.querySelectorAll('input[type="text"]');
        numericInputs.forEach(input => {
            if (input.placeholder.includes('e.g.,') && 
                (input.placeholder.includes('.') || input.placeholder.match(/\d/))) {
                input.addEventListener('input', function(e) {
                    // Allow numbers, dots, and minus signs for scientific notation
                    this.value = this.value.replace(/[^0-9.\-]/g, '');
                });
            }
        });
