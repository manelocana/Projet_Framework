


/* link-path pour utiliser ckeditor-js */

 {/* <script src="https://cdn.ckeditor.com/ckeditor5/38.0.1/classic/ckeditor.js"></script> */}



 /* ckeditor-js to class */
document.addEventListener('DOMContentLoaded', () => {
    const editors = document.querySelectorAll('textarea.ckeditor');

    if (editors.length === 0) return;

    editors.forEach(textarea => {
        ClassicEditor
            .create(textarea)
            .catch(console.error);
    });
});




/* ckeditor - global to ID*/ 
/* document.addEventListener('DOMContentLoaded', () => {
    const editorElement = document.querySelector('#editor');
    const form = document.querySelector('form');

    if (!editorElement || !form) return;

    let editorInstance;

    ClassicEditor
        .create(editorElement)
        .then(editor => {
            editorInstance = editor;
        })
        .catch(console.error);

    form.addEventListener('submit', () => {
        editorElement.value = editorInstance.getData();
    });
}); */




