function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ noteId: noteId }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to delete note.");
      }

      window.location.assign("/");
    })
    .catch((error) => {
      console.error(error);
    });
}
