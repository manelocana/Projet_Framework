

// link-path pour utiliser ckeditor-js --> (end-body)
// <script src="https://cdn.ckeditor.com/ckeditor5/38.0.1/classic/ckeditor.js"></script>



 // ckeditor-js to class
document.addEventListener('DOMContentLoaded', () => {
    const editors = document.querySelectorAll('textarea.ckeditor');

    editors.forEach(textarea => {
        ClassicEditor
            .create(textarea)
            .then(editor => {
                // Guardar el editor en el textarea para submit
                textarea.editorInstance = editor;
            })
            .catch(error => {
        console.error('CKEditor error:', error);
});
    });

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', e => {
            editors.forEach(textarea => {
                if (textarea.editorInstance) {
                    textarea.value = textarea.editorInstance.getData();
                }
            });
        });
    };
});



// flash close in 3 seconds
setTimeout(function() {
    const flashes = document.querySelector('.flash-messages');
    if (flashes) {
        flashes.style.display = 'none';
    }
}, 3000);