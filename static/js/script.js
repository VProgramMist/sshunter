$(
    function () {
        $('.input').on('input',
            function () {
                let free_inp = -1;

                $.each($('.input'), function (index, value) {
                    if (value.value.replace(/ /g, '') === '')
                        free_inp = index;
                });

                if ($('input[name="vsp"]').val().length !== 3)
                    free_inp = 1;

                if (free_inp !== -1)
                    $('.button').prop('disabled', true);
                else $('.button').prop('disabled', false);
            }
        )

        $('input[name="vsp"]').on('input',
            function () {
                $('input[name="vsp"]').mask('000');
            }
        )
    }
)