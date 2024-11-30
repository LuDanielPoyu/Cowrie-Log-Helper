document.addEventListener("DOMContentLoaded", function () {
    const resendButton = document.getElementById("resend-btn");
    const timerText = document.getElementById("timer");
    const isCounting = sessionStorage.getItem("isCounting");

    // 繼續倒計時
    if (isCounting) {
        startCountdown(isCounting);
    }
  
    // 開始倒計時
    function startCountdown(isCounting) {
        let remainingTime = isCounting;
        resendButton.disabled = true; // 禁用按鈕
        timerText.textContent = `in ${remainingTime} seconds`;
    
        const timer = setInterval(() => {
            remainingTime--;
            timerText.textContent = `in ${remainingTime} seconds`;
            sessionStorage.setItem("isCounting", remainingTime);
    
            if (remainingTime <= 0) {
                clearInterval(timer);
                resendButton.disabled = false;
                timerText.textContent = ""; // 清空倒計時
                sessionStorage.removeItem("isCounting");
            }
        }, 1000);
    }
  
    // 按鈕點擊事件
    resendButton.addEventListener("click", function () {
        resendButton.form.submit();
        sessionStorage.setItem("isCounting", 60);
    });
});
  