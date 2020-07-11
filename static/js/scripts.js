const positionLabels = document.getElementsByClassName("position-label");
for (let i = 0; i < positionLabels.length; i++) {
    if (positionLabels[i].textContent === "left-forward") {
        positionLabels[i].textContent = "LF"
    }
    if (positionLabels[i].textContent === "left-centre-forward") {
        positionLabels[i].textContent = "LCF"
    }
    if (positionLabels[i].textContent === "centre-forward") {
        positionLabels[i].textContent = "CF"
    }
    if (positionLabels[i].textContent === "right-centre-forward") {
        positionLabels[i].textContent = "RCF"
    }
    if (positionLabels[i].textContent === "right-forward") {
        positionLabels[i].textContent = "RF"
    }
    if (positionLabels[i].textContent === "left-attacking-midfield") {
        positionLabels[i].textContent = "LAM"
    }
    if (positionLabels[i].textContent === "centre-attacking-midfield") {
        positionLabels[i].textContent = "CAM"
    }
    if (positionLabels[i].textContent === "right-attacking-midfield") {
        positionLabels[i].textContent = "RAM"
    }
    if (positionLabels[i].textContent === "left-midfield") {
        positionLabels[i].textContent = "LM"
    }
    if (positionLabels[i].textContent === "left-centre-midfield") {
        positionLabels[i].textContent = "LCM"
    }
    if (positionLabels[i].textContent === "right-centre-midfield") {
        positionLabels[i].textContent = "RCM"
    }
    if (positionLabels[i].textContent === "right-midfield") {
        positionLabels[i].textContent = "RF"
    }
    if (positionLabels[i].textContent === "left-wing-back") {
        positionLabels[i].textContent = "LWB"
    }
    if (positionLabels[i].textContent === "centre-defensive-midfield") {
        positionLabels[i].textContent = "CDM"
    }
    if (positionLabels[i].textContent === "right-wing-back") {
        positionLabels[i].textContent = "RWB"
    }
    if (positionLabels[i].textContent === "left-back") {
        positionLabels[i].textContent = "LB"
    }
    if ((positionLabels[i].textContent === "back-three-left") || (positionLabels[i].textContent === "left-centre-back")) {
        positionLabels[i].textContent = "LCB"
    }
    if (positionLabels[i].textContent === "centre-back") {
        positionLabels[i].textContent = "CB"
    }
    if ((positionLabels[i].textContent === "right-centre-back") || (positionLabels[i].textContent === "back-three-right")) {
        positionLabels[i].textContent = "RCB"
    }
    if (positionLabels[i].textContent === "right-back") {
        positionLabels[i].textContent = "RB"
    }
    if (positionLabels[i].textContent === "goalkeeper") {
        positionLabels[i].textContent = "GK"
    }
};