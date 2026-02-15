const images = [
  "naco_czas.png",
  "naco_ochota.png",
  "moc1.png",
  "moc2.png",
  "tajemnica_zycia1.png",
  "tajemnica_zycia2.png",
  "tajemnica_zycia3.png",
  "zabawa1.png",
  "zabawa2.png",
  "powrot_do_domu.png",
  "",
//  "naco_czas.png"
];

let currentIndex = 0;

function showImage() {
  document.getElementById("mainImage").src = images[currentIndex];
  if (currentIndex > 3 && currentIndex < 7) {
      const container_o = document.querySelector(".container_opt");
      container_o.innerHTML = `<strong>Życie jest tajemnicą.</strong><br><br>`;
  }
  else if (currentIndex == 9) {
      const container_o = document.querySelector(".container_opt");
      container_o.innerHTML = `<strong>Czym dla mnie jest 'Powrót do domu'?</strong><br><br>`;
  }
  else if (currentIndex > 6 && currentIndex < 9) {
      const container_o = document.querySelector(".container_opt");
      container_o.innerHTML = `<strong>Jak nauczyć na nowo się bawić?</strong><br><br>`;
  }
  else if (currentIndex == 10) {
      const container_o = document.querySelector(".container_opt");
      container_o.innerHTML = `    <video width="640" height="360" controls>
        <source src="na_milosc_nigdy_nie_jest_za_pozno.mp4" type="video/mp4">
        Twoja przeglądarka nie obsługuje odtwarzacza wideo.
    </video>
    <br><br>`;
  }
  else {
      const container_o = document.querySelector(".container_opt");
      container_o.innerHTML = `<br>`;
  }
}

function next() {
  currentIndex++;
  if (currentIndex >= images.length) {
    currentIndex = 0;
  }
  showImage();
}

function prev() {
  currentIndex--;
  if (currentIndex < 0) {
    currentIndex = images.length - 1;
  }
  showImage();
}
