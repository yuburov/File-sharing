const baseUrl = 'http://localhost:8000/api/v1/';

function setUpDepriveAccessButton(fileId, button) {
    button.on('click', function (event) {
        event.preventDefault();
        let data = {
            'id': button.data('id')
        };
        makeRequest(`file/${fileId}/access/deprive/`, 'patch', data).done(
            function (status, message, data) {
                console.log('Successfully deprived access!');
                console.log(status);
                console.log(message);
                button.parent().remove()
            }
        ).fail(
            function (message, status, response) {
                console.log('Could not deprive access to file!');
                console.log(message);
                console.log(status);
                console.log(response);
            }
        )
    })
}

function setUpDepriveAccessButtons() {
    let buttons = $('.depriveAccess');
    buttons.each(function (index) {
        setUpDepriveAccessButton($('#collapseAccessButton').data('file-id'), $(this))
    })
}


function insertErrorMessage(data, inputAfter){
    let errorMessage = $('#accessHelpBlock');
    if (errorMessage.length){
        errorMessage.text(data)
    } else {
        $(`<small id="accessHelpBlock" class="form-error text-muted">${data}</small>`).insertAfter(inputAfter);
    }
}


function addUserLink(data) {
    let form = $('#formAddAccessToUser');
    $(`<div class="btn-group btn-group-sm w-50">
            <a class='btn btn-info' href="http://localhost:8000/accounts/${data.id}/"><i class="far fa-eye"></i> ${ data.username }</a>
            <button id="depriveButton_${data.id}" class="btn btn-danger depriveAccess" data-id="${data.id}"><i class="fas fa-user-slash"></i> Забрать права</button>
    </div>`).insertBefore(form);
    setUpDepriveAccessButton($('#collapseAccessButton').data('file-id'), $(`#depriveButton_${data.id}`))
    let emptyMessage = $('#accessNone');
    if (emptyMessage.length){
        emptyMessage.remove()
    }
}


function setUpProvideUserAccess() {
    let emptyField = $('#accessNone');
    let provideButton = $('#provideAccessSubmit');
    let collapseButton = $('#collapseAccessButton');
    provideButton.on('click', function (event) {
        event.preventDefault();
        let inputField = $('#id_user_name');
        let data = {
            'user_name': inputField.val()
        };
        makeRequest(`file/${collapseButton.data('file-id')}/access/provide`, 'patch', data).done(function (data, status, message) {
            console.log('Пользователь получил доступ!');
            console.log(data);
            console.log(status);
            console.log(message);
            addUserLink(data);
            inputField.val("")
        }).fail(function (response, message, wtf) {
            console.log('Нe удалось предоставить доступ!');
            insertErrorMessage(response.responseJSON.message, $('.input-group'));
            console.log(message);
            console.log(response.responseJSON.message);
            console.log(wtf);
        })

    })
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path;
}

function makeRequest(path, method, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    return $.ajax(settings);
}

$(document).ready(function() {
    setUpProvideUserAccess();
    setUpDepriveAccessButtons();
});