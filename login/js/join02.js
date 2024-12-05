// 비밀번호 text -> password 변경

        // 모든 버튼 및 입력 필드를 가져옵니다.
        const passwordFields = document.querySelectorAll('.join2_input1');
        const toggleButtons = document.querySelectorAll('.toggleButton');
        
        // 각 버튼에 이벤트 리스너 추가
        toggleButtons.forEach((button, index) => {
          const toggleImage = button.querySelector('img'); // 버튼 내부의 이미지
          const passwordField = passwordFields[index]; // 해당 버튼에 맞는 입력 필드
          
          button.addEventListener('click', () => {
            // 현재 필드 타입 확인 및 토글
            if (passwordField.type === 'password') {
              passwordField.type = 'text'; // 텍스트로 변경
              toggleImage.src = '../images/eye_open.png'; // 눈 열림 이미지
              toggleImage.alt = '비밀번호 숨기기';
            } else {
              passwordField.type = 'password'; // 비밀번호로 변경
              toggleImage.src = '../images/eye_closed.png'; // 눈 닫힘 이미지
              toggleImage.alt = '비밀번호 보기';
            }
          });
        });
        



        // 비밀번호 필요조건

        const validateButton = document.getElementById('join2_button');
        const passwordInput = document.getElementById('join02_password');
            // 비밀번호 유효성 검사 함수
        function validatePassword(password) {
          const regex = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:'",.<>?]).{8,12}$/;
          return regex.test(password);
        }
        // 버튼 클릭 이벤트
        validateButton.addEventListener('click', () => {
          const password = passwordInput.value;
          alert('8자 이상 12자리 이하의 숫자, 영문자, 특수문자를 포함해주세요.')
        });




        // 비밀번호 확인기능
        const checkButton = document.getElementById('join2_button');
        const pwpw = document.getElementById('join02_password');
        const pwpw2 = document.getElementById('join02_password2');
    
        // 버튼 클릭 이벤트
        validateButton.addEventListener('click', () => {
          if (pwpw.value === pwpw2.value) {
            pass
          } else {
            alert('비밀번호가 일치하지 않습니다.');
          }
        });



// input이 비었을때 에러메세지

const join2submitButton = document.getElementById('join2_button');
const inputs = document.querySelectorAll('.join2_input');
const join21errorMessage = document.querySelectorAll('.join2_error-message');

// 버튼 클릭 시 입력 필드 확인
join2_button.addEventListener('click', () => {
  let isValid = true;

  // 입력 필드 확인
  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].value.trim() === '') {
      join21errorMessage[i].style.display = 'block'; // 에러 메시지 표시
      if (isValid) {
        inputs[i].focus(); // 첫 번째 비어 있는 필드에 포커스
      }
      isValid = false;
    } else {
      join21errorMessage[i].style.display = 'none'; // 에러 메시지 숨김
    }
  }
});

// 입력 필드에 포커스를 잃었을 때도 확인
inputs.forEach((input, index) => {
  input.addEventListener('blur', () => {
    if (input.value.trim() === '') {
      join21errorMessage[index].style.display = 'block';
    } else {
      join21errorMessage[index].style.display = 'none';
    }
  });
});