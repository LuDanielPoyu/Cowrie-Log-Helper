// 選擇登出按鈕
const logoutButton = document.getElementById('logoutButton');

// 在按鈕點擊時清除 sessionStorage
logoutButton.addEventListener('click', function() {
    sessionStorage.removeItem("histState");
});