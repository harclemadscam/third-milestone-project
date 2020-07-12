//loads on lineup page
//loops through position labels, checks text content and updates it, adds css class
const positionLabels = document.getElementsByClassName("position-label");
for (let i = 0; i < positionLabels.length; i++) {
    if (positionLabels[i].textContent === "left-forward") {
        positionLabels[i].textContent = "LF";
        positionLabels[i].classList.add("forward-label");
    }
    if (positionLabels[i].textContent === "left-centre-forward") {
        positionLabels[i].textContent = "LCF";
        positionLabels[i].classList.add("forward-label");

    }
    if (positionLabels[i].textContent === "centre-forward") {
        positionLabels[i].textContent = "CF";
        positionLabels[i].classList.add("forward-label");
    }
    if (positionLabels[i].textContent === "right-centre-forward") {
        positionLabels[i].textContent = "RCF";
        positionLabels[i].classList.add("forward-label");
    }
    if (positionLabels[i].textContent === "right-forward") {
        positionLabels[i].textContent = "RF";
        positionLabels[i].classList.add("forward-label");
    }
    if (positionLabels[i].textContent === "left-attacking-midfield") {
        positionLabels[i].textContent = "LAM";
        positionLabels[i].classList.add("attacking-mid-label");
    }
    if (positionLabels[i].textContent === "centre-attacking-midfield") {
        positionLabels[i].textContent = "CAM";
        positionLabels[i].classList.add("attacking-mid-label");
    }
    if (positionLabels[i].textContent === "right-attacking-midfield") {
        positionLabels[i].textContent = "RAM";
        positionLabels[i].classList.add("attacking-mid-label");
    }
    if (positionLabels[i].textContent === "left-midfield") {
        positionLabels[i].textContent = "LM";
        positionLabels[i].classList.add("midfield-label");
    }
    if (positionLabels[i].textContent === "left-centre-midfield") {
        positionLabels[i].textContent = "LCM";
        positionLabels[i].classList.add("midfield-label");
    }
    if (positionLabels[i].textContent === "right-centre-midfield") {
        positionLabels[i].textContent = "RCM";
        positionLabels[i].classList.add("midfield-label");
    }
    if (positionLabels[i].textContent === "right-midfield") {
        positionLabels[i].textContent = "RM";
        positionLabels[i].classList.add("midfield-label");
    }
    if (positionLabels[i].textContent === "left-wing-back") {
        positionLabels[i].textContent = "LWB";
        positionLabels[i].classList.add("wing-back-label");
    }
    if (positionLabels[i].textContent === "centre-defensive-midfield") {
        positionLabels[i].textContent = "CDM";
        positionLabels[i].classList.add("midfield-label");
    }
    if (positionLabels[i].textContent === "right-wing-back") {
        positionLabels[i].textContent = "RWB";
        positionLabels[i].classList.add("wing-back-label");
    }
    if (positionLabels[i].textContent === "left-back") {
        positionLabels[i].textContent = "LB";
        positionLabels[i].classList.add("defence-label");
    }
    if ((positionLabels[i].textContent === "back-three-left") || (positionLabels[i].textContent === "left-centre-back")) {
        positionLabels[i].textContent = "LCB";
        positionLabels[i].classList.add("defence-label");
    }
    if (positionLabels[i].textContent === "centre-back") {
        positionLabels[i].textContent = "CB";
        positionLabels[i].classList.add("defence-label");
    }
    if ((positionLabels[i].textContent === "right-centre-back") || (positionLabels[i].textContent === "back-three-right")) {
        positionLabels[i].textContent = "RCB";
        positionLabels[i].classList.add("defence-label");
    }
    if (positionLabels[i].textContent === "right-back") {
        positionLabels[i].textContent = "RB";
        positionLabels[i].classList.add("defence-label");
    }
    if (positionLabels[i].textContent === "goalkeeper") {
        positionLabels[i].textContent = "GK";
        positionLabels[i].classList.add("goalkeeper-label");
    }
}