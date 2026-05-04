document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('email-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const btnText = document.querySelector('.btn-text');
    const spinner = document.getElementById('loading-spinner');
    
    const resultsPanel = document.getElementById('results-panel');
    const statusBadge = document.getElementById('status-badge');
    
    const probPhishingTxt = document.getElementById('prob-phishing');
    const probSafeTxt = document.getElementById('prob-safe');
    const fillPhishing = document.getElementById('fill-phishing');
    const fillSafe = document.getElementById('fill-safe');
    
    const errorMessage = document.getElementById('error-message');

    analyzeBtn.addEventListener('click', async () => {
        const text = emailInput.value.trim();
        if (!text) {
            showError("Please enter some email text to analyze.");
            return;
        }

        // Reset UI
        errorMessage.classList.add('hidden');
        resultsPanel.classList.add('hidden');
        
        // Set loading state
        analyzeBtn.disabled = true;
        btnText.textContent = "Analyzing...";
        spinner.classList.remove('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "An error occurred during analysis.");
            }

            // Update UI with results
            displayResults(data);

        } catch (error) {
            showError(error.message);
        } finally {
            // Remove loading state
            analyzeBtn.disabled = false;
            btnText.textContent = "Analyze Email";
            spinner.classList.add('hidden');
        }
    });

    function displayResults(data) {
        resultsPanel.classList.remove('hidden');
        
        const prediction = data.prediction;
        const probs = data.probabilities;
        
        const pPhishing = (probs['Phishing'] * 100).toFixed(1);
        const pSafe = (probs['Safe'] * 100).toFixed(1);

        // Update badge
        statusBadge.textContent = prediction;
        if (prediction === 'Phishing') {
            statusBadge.className = 'badge phishing';
        } else {
            statusBadge.className = 'badge safe';
        }

        // Animate bars (timeout ensures CSS transition triggers after display:block)
        setTimeout(() => {
            probPhishingTxt.textContent = `${pPhishing}%`;
            fillPhishing.style.width = `${pPhishing}%`;
            
            probSafeTxt.textContent = `${pSafe}%`;
            fillSafe.style.width = `${pSafe}%`;
        }, 50);
    }

    function showError(msg) {
        errorMessage.textContent = msg;
        errorMessage.classList.remove('hidden');
    }
});
