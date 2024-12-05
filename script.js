document.getElementById('submitButton').addEventListener('click', () => {
  const radios = document.querySelectorAll('input[name="option"]');
  const warningMessage = document.getElementById('warningMessage');

  // 라디오 버튼 중 선택된 것이 있는지 확인
  const isChecked = Array.from(radios).some(radio => radio.checked);

  if (!isChecked) {
    // 경고 메시지 표시
    warningMessage.textContent = '옵션을 선택해주세요!';
  } else {
    // 경고 메시지 숨기기 및 제출 처리
    warningMessage.textContent = '';
    alert('제출 완료!');
  }
});
