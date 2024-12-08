const toggleBtn_1 = document.querySelector('#toggle-btn-1');
const toggleBtn_2 = document.querySelector('#toggle-btn-2');
const navLinks_1 = document.querySelector('#nav-links-1');
const navLinks_2 = document.querySelector('#nav-links-2');
const toggleImg_1 = document.querySelector('#toggle-img-1');
const toggleImg_2 = document.querySelector('#toggle-img-2');
const histBtn = document.querySelector('#toggle-btn-hist');
const histLink = document.querySelector('#hist-link');

const expandIcon = '/static/images/minus.png'; // 展開時的圖示
const collapseIcon = '/static/images/plus.png'; // 收合時的圖示
const histExpandIcon = '/static/images/triangle-rotate.png'; // 展開時的圖示
const histCollapseIcon = '/static/images/triangle.png'; // 收合時的圖示

function expand(navLink, img, icon) {
    navLink.classList.remove('hide');
    navLink.style.height = navLink.scrollHeight + 'px';
    img.src = icon;
}

function collapse(navLink, img, icon) {
    navLink.classList.add('hide');
    navLink.style.height = '0';
    navLink.style.overflow = 'hidden';
    img.src = icon;
}

function collapseWithAnimation(navLink, img, icon) {
    navLink.classList.add('hide');
    navLink.style.height = navLink.scrollHeight + 'px'; // 設置高度為當前高度（觸發動畫）
    requestAnimationFrame(() => {
        navLink.style.height = '0'; // 收合為 0
    });
    img.src = icon;
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
        collapse(navLinks_1, toggleImg_1, collapseIcon);
    } else {
        // 如果之前展開，設置為展開
        expand(navLinks_1, toggleImg_1, expandIcon);
    }

    stored_session_state_2 = sessionStorage.getItem('navState_2');
    if (stored_session_state_2 === 'collapsed') {
        collapse(navLinks_2, toggleImg_2, collapseIcon);
    } else {
        expand(navLinks_2, toggleImg_2, expandIcon);
    }

    hist_session_state = sessionStorage.getItem('histNavState');
    if (hist_session_state === 'collapsed') {
        collapse(histLink, histBtn, histCollapseIcon);
    } else {
        expand(histLink, histBtn, histExpandIcon);
    }
    
} else {
    // 來自上面三個頁面就一律展開
    expand(navLinks_1, toggleImg_1, expandIcon);
    sessionStorage.setItem('navState_1', 'expanded');

    expand(navLinks_2, toggleImg_2, expandIcon);
    sessionStorage.setItem('navState_2', 'expanded');

    expand(histLink, histBtn, histExpandIcon);
    sessionStorage.setItem('histNavState', 'expanded');
}

toggleBtn_1.addEventListener('click', () => {
    if (navLinks_1.classList.contains('hide')) {
        // 展開
        expand(navLinks_1, toggleImg_1, expandIcon);
        sessionStorage.setItem('navState_1', 'expanded');
    } else {
        // 收合
        collapseWithAnimation(navLinks_1, toggleImg_1, collapseIcon);
        sessionStorage.setItem('navState_1', 'collapsed');
    } 
});

toggleBtn_2.addEventListener('click', () => {
    if (navLinks_2.classList.contains('hide')) {
        // 展開
        expand(navLinks_2, toggleImg_2, expandIcon);
        sessionStorage.setItem('navState_2', 'expanded');
    } else {
        // 收合
        collapseWithAnimation(navLinks_2, toggleImg_2, collapseIcon);
        sessionStorage.setItem('navState_2', 'collapsed');
    }
});

histBtn.addEventListener('click', () => {
    if (histLink.classList.contains('hide')) {
        // 展開
        expand(histLink, histBtn, histExpandIcon);
        sessionStorage.setItem('histNavState', 'expanded');
    } else {
        // 收合
        collapseWithAnimation(histLink, histBtn, histCollapseIcon);
        sessionStorage.setItem('histNavState', 'collapsed');
    }
});