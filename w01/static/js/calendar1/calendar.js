    const modal = document.getElementById('myModal');
    const openModalBtn = document.getElementById('openModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');

    openModalBtn.addEventListener('click', () => {
        modal.style.display = 'flex'; // 모달을 보이게 설정
    });

    closeModalBtn.addEventListener('click', () => {
        modal.style.display = 'none'; // 모달을 숨김
    });

    // 모달 바깥을 클릭하면 닫히도록 처리
    modal.addEventListener('click', (event) => {
      if (event.target === modal) {
          modal.style.display = 'none';
      }
    });

