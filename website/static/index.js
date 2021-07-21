function deleteNote(note_id, current_user_id){

    delobj = {noteId : note_id, userId : current_user_id};

    fetch("/delete-note",{
        method:"POST",
        body:JSON.stringify(delobj),
    }).then((_res) => {
        window.location.href = "/";
    })
}
