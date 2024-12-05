// 아이디찾기 페이지1

// input이 비었을때 에러메세지

const join3submitButton = document.getElementById('join03button');
const inputs = document.querySelectorAll('.join3_input');
const join31errorMessage = document.querySelectorAll('.join3_error-message');

// 버튼 클릭 시 입력 필드 확인
join03button.addEventListener('click', () => {
  let isValid = true;

  // 입력 필드 확인
  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].value.trim() === '') {
      join31errorMessage[i].style.display = 'block'; // 에러 메시지 표시
      if (isValid) {
        inputs[i].focus(); // 첫 번째 비어 있는 필드에 포커스
      }
      isValid = false;
    } else {
      join31errorMessage[i].style.display = 'none'; // 에러 메시지 숨김
    }
  }
});

// 입력 필드에 포커스를 잃었을 때도 확인
inputs.forEach((input, index) => {
  input.addEventListener('blur', () => {
    if (input.value.trim() === '') {
      join31errorMessage[index].style.display = 'block';
    } else {
      join31errorMessage[index].style.display = 'none';
    }
  });
});

//radio 비어있을시
document.getElementById('join03button').addEventListener('click', () => {
  const radios = document.querySelectorAll('input[name="gender"]');
  const join3_errorMessage3 = document.getElementById('join3_errorMessage3');

  // 라디오 버튼 중 선택된 것이 있는지 확인
  const isChecked = Array.from(radios).some(radio => radio.checked);

  if (!isChecked) {
    join3_errorMessage3.style.display = 'block';
    pwpw.focus(); // 첫 번째 입력 필드에 포커스 이동
    isValid = false;
  } else {
    join3_errorMessage3.style.display = 'none';
  }
});

