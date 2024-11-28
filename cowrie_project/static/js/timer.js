document.addEventListener("DOMContentLoaded", function () {
    const resendButton = document.getElementById("resend-btn");
    const timerText = document.getElementById("timer");
    let countdown = 60;
  
    // 啟用按鈕
    function enableButton() {
      resendButton.disabled = false;
      resendButton.textContent = "Resend Code";
      timerText.style.display = "none"; // 隱藏倒計時文字
    }
  
    // 開始倒計時
    function startCountdown() {
      resendButton.disabled = true; // 禁用按鈕
      timerText.style.display = "block"; // 顯示倒計時文字
      timerText.textContent = `in ${countdown} seconds`;
  
      const timer = setInterval(() => {
        countdown--;
        timerText.textContent = `in ${countdown} seconds`;
  
        if (countdown <= 0) {
          clearInterval(timer);
          enableButton();
          countdown = 60; // 重置倒計時
        }
      }, 1000);
    }
  
    // 按鈕點擊事件
    resendButton.addEventListener("click", function () {
      alert("Verification code has been resent！");
      startCountdown();
    });
  });
  