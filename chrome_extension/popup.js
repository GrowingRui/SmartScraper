document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('runBtn');
    const statusDiv = document.getElementById('status');

    btn.onclick = async () => {
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        statusDiv.innerText = "发送请求中...";

        try {
            const response = await fetch('http://127.0.0.1:5000/scrape', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: tab.url })
            });
            const data = await response.json();
            statusDiv.innerText = data.message;
        } catch (error) {
            statusDiv.innerText = "错误：请检查后端服务";
        }
    };
});