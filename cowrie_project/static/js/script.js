const toggleBtn_1 = document.querySelector('#toggle-btn-1');
const toggleBtn_2 = document.querySelector('#toggle-btn-2');
const navLinks_1 = document.querySelector('#nav-links-1');
const navLinks_2 = document.querySelector('#nav-links-2');
const toggleImg_1 = document.querySelector('#toggle-img-1');
const toggleImg_2 = document.querySelector('#toggle-img-2');

const expandIcon = '/static/images/minus.png'; // 展開時的圖示
const collapseIcon = '/static/images/plus.png'; // 收合時的圖示

function expand(navLink, img) {
    navLink.classList.remove('hide');
    navLink.style.height = navLink.scrollHeight + 'px';
    img.src = expandIcon;
}

function collapse(navLink, img) {
    navLink.classList.add('hide');
    navLink.style.height = '0';
    navLink.style.overflow = 'hidden';
    img.src = collapseIcon;
}

function collapseWithAnimation(navLink, img) {
    navLink.classList.add('hide');
    navLink.style.height = navLink.scrollHeight + 'px'; // 設置高度為當前高度（觸發動畫）
    requestAnimationFrame(() => {
        navLink.style.height = '0'; // 收合為 0
    });
    img.src = collapseIcon;
}

let url_list = [
    "http://127.0.0.1:8000/", 
    "http://127.0.0.1:8000/users/login/", 
    "http://127.0.0.1:8000/users/register/"
]

// 非來自上面三個頁面就依之前的狀態
if (!url_list.includes(document.referrer)) {
    stored_session_state_1 = sessionStorage.getItem('navState_1');
    if (stored_session_state_1 === 'collapsed') {
        // 如果之前收合，設置為隱藏
        collapse(navLinks_1, toggleImg_1);
    } else {
        // 如果之前展開，設置為展開
        expand(navLinks_1, toggleImg_1);
    }

    stored_session_state_2 = sessionStorage.getItem('navState_2');
    if (stored_session_state_2 === 'collapsed') {
        collapse(navLinks_2, toggleImg_2);
    } else {
        expand(navLinks_2, toggleImg_2);
    }
    
} else {
    // 來自上面三個頁面就一律展開
    expand(navLinks_1, toggleImg_1);
    sessionStorage.setItem('navState_1', 'expanded');

    expand(navLinks_2, toggleImg_2);
    sessionStorage.setItem('navState_2', 'expanded');
}

toggleBtn_1.addEventListener('click', () => {
    if (navLinks_1.classList.contains('hide')) {
        // 展開
        expand(navLinks_1, toggleImg_1);
        sessionStorage.setItem('navState_1', 'expanded');
    } else {
        // 收合
        collapseWithAnimation(navLinks_1, toggleImg_1);
        sessionStorage.setItem('navState_1', 'collapsed');
    } 
});

toggleBtn_2.addEventListener('click', () => {
    if (navLinks_2.classList.contains('hide')) {
        // 展開
        expand(navLinks_2, toggleImg_2);
        sessionStorage.setItem('navState_2', 'expanded');
    } else {
        // 收合
        collapseWithAnimation(navLinks_2, toggleImg_2);
        sessionStorage.setItem('navState_2', 'collapsed');
    }
});