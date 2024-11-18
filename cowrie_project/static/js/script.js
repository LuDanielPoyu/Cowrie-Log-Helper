const toggleBtn_1 = document.querySelector('#toggle-btn-1');
const toggleBtn_2 = document.querySelector('#toggle-btn-2');
const navLinks_1 = document.querySelector('#nav-links-1');
const navLinks_2 = document.querySelector('#nav-links-2');
const toggleImg_1 = document.querySelector('#toggle-img-1');
const toggleImg_2 = document.querySelector('#toggle-img-2');

const expandIcon = '/static/images/minus.png'; // 展開時的圖示
const collapseIcon = '/static/images/plus.png'; // 收合時的圖示

let url_list = ["http://127.0.0.1:8000/", "http://127.0.0.1:8000/about/", 
                "http://127.0.0.1:8000/users/login/", "http://127.0.0.1:8000/users/register/"]

if (!url_list.includes(document.referrer)) {
    stored_session_state_1 = sessionStorage.getItem('navState_1')
    if (stored_session_state_1 === 'collapsed') {
        // 如果之前收合，則直接設置為隱藏
        navLinks_1.classList.add('hide');
        navLinks_1.style.height = '0';
        navLinks_1.style.overflow = 'hidden';
        toggleImg_1.src = collapseIcon;
    } else {
        // 否則，設置為展開狀態
        navLinks_1.classList.remove('hide');
        navLinks_1.style.height = navLinks_1.scrollHeight + 'px';
        toggleImg_1.src = expandIcon;
    }

    stored_session_state_2 = sessionStorage.getItem('navState_2')
    if (stored_session_state_2 === 'collapsed') {
        // 如果之前收合，則直接設置為隱藏
        navLinks_2.classList.add('hide');
        navLinks_2.style.height = '0';
        navLinks_2.style.overflow = 'hidden';
        toggleImg_2.src = collapseIcon;
    } else {
        // 否則，設置為展開狀態
        navLinks_2.classList.remove('hide');
        navLinks_2.style.height = navLinks_2.scrollHeight + 'px';
        toggleImg_2.src = expandIcon;
    }
    
} else {
    navLinks_1.classList.remove('hide');
    navLinks_1.style.height = navLinks_1.scrollHeight + 'px';
    toggleImg_1.src = expandIcon;
    sessionStorage.setItem('navState_1', 'expanded');

    navLinks_2.classList.remove('hide');
    navLinks_2.style.height = navLinks_2.scrollHeight + 'px';
    toggleImg_2.src = expandIcon;
    sessionStorage.setItem('navState_2', 'expanded');
}

toggleBtn_1.addEventListener('click', () => {
    if (navLinks_1.classList.contains('hide')) {
        // 展開
        navLinks_1.classList.remove('hide');
        navLinks_1.style.height = navLinks_1.scrollHeight + 'px'; // 設置為自動高度
        toggleImg_1.src = expandIcon;
        sessionStorage.setItem('navState_1', 'expanded');
    } else {
        // 收合
        navLinks_1.style.height = navLinks_1.scrollHeight + 'px'; // 設置高度為當前高度（觸發動畫）
        requestAnimationFrame(() => {
            navLinks_1.style.height = '0'; // 收合為 0
        });
        navLinks_1.classList.add('hide');
        toggleImg_1.src = collapseIcon;
        sessionStorage.setItem('navState_1', 'collapsed');
    } 
});

toggleBtn_2.addEventListener('click', () => {
    if (navLinks_2.classList.contains('hide')) {
        // 展開
        navLinks_2.classList.remove('hide');
        navLinks_2.style.height = navLinks_2.scrollHeight + 'px'; // 設置為自動高度
        toggleImg_2.src = expandIcon;
        sessionStorage.setItem('navState_2', 'expanded');
    } else {
        // 收合
        navLinks_2.style.height = navLinks_2.scrollHeight + 'px'; // 設置高度為當前高度（觸發動畫）
        requestAnimationFrame(() => {
            navLinks_2.style.height = '0'; // 收合為 0
        });
        navLinks_2.classList.add('hide');
        toggleImg_2.src = collapseIcon;
        sessionStorage.setItem('navState_2', 'collapsed');
    }
});

navLinks_1.addEventListener('transitionend', () => {
    if (!navLinks_1.classList.contains('hide')) {
        navLinks_1.style.height = 'auto';
    }
});

navLinks_2.addEventListener('transitionend', () => {
    if (!navLinks_2.classList.contains('hide')) {
        navLinks_2.style.height = 'auto';
    }
});