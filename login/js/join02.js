

// 아이디찾기 페이지1

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