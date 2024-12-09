// 변수 선언
const loginButton = document.getElementById('login_button');
const idInput = document.getElementById('id_input');
const pwInput = document.getElementById('pw_input');
const loginErrorMessage1 = document.getElementById('login_errorMessage1');
const loginErrorMessage2 = document.getElementById('login_errorMessage2');
const rememberCheckbox = document.getElementById('remember');

// 페이지 로드 시 쿠키에서 아이디를 가져와 자동으로 설정
window.onload = function() {
  const storedId = getCookie('user_id');
  if (storedId) {
    idInput.value = storedId;
    rememberCheckbox.checked = true;  // 체크박스 체크 상태 유지
  }
};

// 로그인 버튼 클릭 시 입력 필드 확인
loginButton.addEventListener('click', () => {
  let isValid = true;

  // 아이디 입력 확인
  if (idInput.value.trim() === '') {
    loginErrorMessage1.style.display = 'block';
    idInput.focus();
    isValid = false;
  } else {
    loginErrorMessage1.style.display = 'none';
  }

  // 비밀번호 입력 확인
  if (pwInput.value.trim() === '') {
    if (idInput.value.trim() !== '') {
      loginErrorMessage2.style.display = 'block';
      pwInput.focus();
    }
    isValid = false;
  } else {
    loginErrorMessage2.style.display = 'none';
  }

  // 유효한 경우 로그인 폼 제출
  if (isValid) {
    loginFrm.submit();
  }
});

// 입력 필드에서 포커스가 벗어날 때 에러 메시지 확인
idInput.addEventListener('blur', () => {
  if (idInput.value.trim() === '') {
    loginErrorMessage1.style.display = 'block';
  } else {
    loginErrorMessage1.style.display = 'none';
  }
});

pwInput.addEventListener('blur', () => {
  if (pwInput.value.trim() === '') {
    loginErrorMessage2.style.display = 'block';
  } else {
    loginErrorMessage2.style.display = 'none';
  }
});

// 체크박스 상태에 따라 쿠키에 아이디 저장
loginButton.addEventListener('click', () => {
  if (rememberCheckbox.checked) {
    setCookie('user_id', idInput.value, 7);  // 7일 동안 쿠키 저장
  } else {
    deleteCookie('user_id');
  }
});

// 쿠키 설정 함수
function setCookie(name, value, days) {
  const expires = new Date();
  expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));  // 날짜 계산
  document.cookie = `${name}=${value}; expires=${expires.toUTCString()}; path=/`;
}

// 쿠키 가져오기 함수
function getCookie(name) {
  const nameEQ = `${name}=`;
  const ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i].trim();
    if (c.indexOf(nameEQ) === 0) {
      return c.substring(nameEQ.length, c.length);
    }
  }
  return null;
}

// 쿠키 삭제 함수
function deleteCookie(name) {
  document.cookie = `${name}=; Max-Age=-99999999; path=/`;
}
