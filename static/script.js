document.addEventListener("DOMContentLoaded", function () {
    const ajoutEleveLink = document.getElementById("ajout-eleve-link");
    const ajoutEleveModal = document.getElementById("ajout-eleve-modal");
    const ajoutNoteLink = document.getElementById("ajout-note-link");
    const ajoutNoteModal = document.getElementById("ajout-note-modal");
    const closeModalButton = document.getElementById("close-eleve-modal");
    const closeNoteButton = document.getElementById("close-note-modal");
    
    ajoutEleveLink.addEventListener("click", function (event) {
        event.preventDefault();
        ajoutEleveModal.style.display = "block";
    });

    closeModalButton.addEventListener("click", function () {
        ajoutEleveModal.style.display = "none";
    });

    ajoutNoteLink.addEventListener("click", function (event) {
        event.preventDefault();
        ajoutNoteModal.style.display = "block";
    });

    closeNoteButton.addEventListener("click", function () {
        ajoutNoteModal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === ajoutEleveModal) {
            ajoutEleveModal.style.display = "none";
        }
        
        if (event.target === ajoutNoteModal) {
            ajoutNoteModal.style.display = "none";
        }
    });
});
