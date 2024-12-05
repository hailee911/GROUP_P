// 비밀번호 text -> password 변경

        // 모든 버튼 및 입력 필드를 가져옵니다.
        const passwordFields = document.querySelectorAll('.pw3_id_input');
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

        const validateButton = document.getElementById('validateButton');
        const passwordInput = document.getElementById('pwpw');
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
        const checkButton = document.getElementById('validateButton');
        const pwpw = document.getElementById('pwpw');
        const pwpw2 = document.getElementById('pwpw2');
    
        // 버튼 클릭 이벤트
        validateButton.addEventListener('click', () => {
          if (pwpw.value === pwpw2.value) {
            pass
          } else {
            alert('비밀번호가 일치하지 않습니다.');
          }
        });




        
        // input이 비었을때 에러메세지

        const submitButton = document.getElementById('validateButton');
        const textInput1 = document.getElementById('pwpw');
        const textInput2 = document.getElementById('pwpw2');
        const errorMessage1 = document.getElementById('errorMessage1');
        const errorMessage2 = document.getElementById('errorMessage2');
    
        // 버튼 클릭 시 입력 필드 확인
        validateButton.addEventListener('click', () => {
          let isValid = true;
    
          // 첫 번째 입력 필드 확인
          if (pwpw.value.trim() === '') {
            errorMessage1.style.display = 'block';
            pwpw.focus(); // 첫 번째 입력 필드에 포커스 이동
            isValid = false;
          } else {
            errorMessage1.style.display = 'none';
          }
    
          // 두 번째 입력 필드 확인
          if (pwpw2.value.trim() === '') {
            errorMessage2.style.display = 'block';
            if (isValid) {
              pwpw2.focus(); // 첫 번째 입력 필드가 비어있지 않으면 두 번째로 포커스 이동
            }
            isValid = false;
          } else {
            errorMessage2.style.display = 'none';
          }
    
        });
    
        // 입력 필드에 포커스를 잃었을 때도 확인
        pwpw.addEventListener('blur', () => {
          if (pwpw.value.trim() === '') {
            errorMessage1.style.display = 'block';
          } else {
            errorMessage1.style.display = 'none';
          }
        });
    
        pwpw2.addEventListener('blur', () => {
          if (pwpw2.value.trim() === '') {
            errorMessage2.style.display = 'block';
          } else {
            errorMessage2.style.display = 'none';
          }
        });