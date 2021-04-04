<template>
    <div id="form">
        <div class="title" id="divider">
            Подать заявку
        </div><br>
        <div class="input-container">
            <select :class="{'error' : $v.school.$error}" :disabled="disabledFields" id="school" v-model.trim="$v.school.$model">
                <option value="" selected disabled hidden>Выбери твою школу</option>
                <option value="Средняя школа №1">Средняя школа №1</option>
                <option value="Средняя школа №2">Средняя школа №2</option>
                <option value="Средняя школа №3">Средняя школа №3</option>
                <option value="Средняя школа №4">Средняя школа №4</option>
                <option value="Средняя школа №5">Средняя школа №5</option>
                <option value="Средняя школа №6">Средняя школа №6</option>
                <option value="Средняя школа №7">Средняя школа №7</option>
                <option value="Средняя школа №8">Средняя школа №8</option>
                <option value="Средняя школа №9">Средняя школа №9</option>
                <option value="Средняя школа №10">Средняя школа №10</option>
                <option value="Средняя школа №11">Средняя школа №11</option>
                <option value="Гимназия им. Горького">Гимназия им. Горького</option>
                <option value="Средняя школа №13">Средняя школа №13</option>
                <option value="Средняя школа №14">Средняя школа №14</option>
                <option value="Средняя школа №15">Средняя школа №15</option>
                <option value="Средняя школа №16">Средняя школа №16</option>
                <option value="Средняя школа №17">Средняя школа №17</option>
                <option value="Средняя школа №18">Средняя школа №18</option>
                <option value="Средняя школа №19">Средняя школа №19</option>
                <option value="Средняя школа №20">Средняя школа №20</option>
                <option value="Средняя школа №21">Средняя школа №21</option>
                <option value="Средняя школа №22">Средняя школа №22</option>
                <option value="Средняя школа №23">Средняя школа №23</option>
                <option value="Гимназия им. Мауленова">Гимназия им. Мауленова</option>
                <option value="Средняя школа №25">Средняя школа №25</option>
                <option value="Физико-Математический Лицей">Физико-Математический Лицей</option>
                <option value="Средняя школа №30">Средняя школа №30</option>
                <option value="Средняя школа №115">Средняя школа №115</option>
                <option value="Средняя школа №122">Средняя школа №122</option>
                <option value="Дружбинская средняя школа">Дружбинская средняя школа</option>
                <option value="УМЦ НВП">УМЦ НВП</option>
                <option value="Вечерняя школа №1">Вечерняя школа №1</option>
                <option value="Средняя школа г. Тобыл">Средняя школа г. Тобыл</option>
                <option value="Средняя школа п. Заречный">Средняя школа п. Заречный</option>
                <option value="Средняя школа п. Мичурино">Средняя школа п. Мичурино</option>
                <option value="Алтынсаринский район">Алтынсаринский район</option>
                <option value="Амангельдинский район">Амангельдинский район</option>
                <option value="Аулиекольский район">Аулиекольский район</option>
                <option value="Денисовский район">Денисовский район</option>
                <option value="Джангельдинский район">Джангельдинский район</option>
                <option value="Житикаринский район">Житикаринский район</option>
                <option value="Камыстинский район">Камыстинский район</option>
                <option value="Карабалыкский район">Карабалыкский район</option>
                <option value="Карасуский район">Карасуский район</option>
                <option value="Костанайский район">Костанайский район</option>
                <option value="Мендыгаринский район">Мендыгаринский район</option>
                <option value="Наурзумский район">Наурзумский район</option>
                <option value="Сарыкольский район ">Сарыкольский район </option>
                <option value="Тарановский район">Тарановский район</option>
                <option value="Узункольский район">Узункольский район</option>
                <option value="Федоровский район">Федоровский район</option>
                <option value="г. Аркалык">г. Аркалык</option>
                <option value="г. Лисаковск">г. Лисаковск</option>
                <option value="г. Рудный">г. Рудный</option>
                <option value="Другое">Другое</option>
            </select><br>
            <span class="error-text" v-if="$v.school.$dirty && !$v.school.required">Это поле обязательно для заполнения</span>
        </div>
        <div class="input-container">
            <input :class="{'error' : $v.fullname.$error}" :disabled="disabledFields" placeholder="ФИО" maxlength="64" id="fullname" v-model.trim="$v.fullname.$model"><br>
            <span class="error-text" v-if="$v.fullname.$dirty && !$v.fullname.required">Это поле обязательно для заполнения</span>
        </div>
        <div class="input-container">
            <input :class="{'error' : $v.phone.$error}" :disabled="disabledFields" placeholder="Твой номер телефона" type="phone" maxlength="16" id="phone" v-model.trim="$v.phone.$model"><br>
            <span class="error-text" v-if="$v.phone.$dirty && !$v.phone.required">Это поле обязательно для заполнения</span>
        </div>
        <div class="input-container">
            <input :class="{'error' : $v.email.$error}" :disabled="disabledFields" placeholder="Твой email" type="email" maxlength="64" id="email" v-model.trim="$v.email.$model"><br>
            <span class="error-text" v-if="$v.email.$dirty && !$v.email.required">Это поле обязательно для заполнения</span>
        </div>
        <div class="input-container">
            <input :class="{'error' : $v.group.$error}" :disabled="disabledFields" placeholder="Твой класс (9A, 9Б, ...)" maxlength="16" id="group" v-model.trim="$v.group.$model"><br>
            <span class="error-text" v-if="$v.group.$dirty && !$v.group.required">Это поле обязательно для заполнения</span>
        </div>
        <div class="input-container">
            <input :class="{'error' : $v.nickname.$error}" :disabled="disabledFields" placeholder="Твой ник в игре" maxlength="16" id="nickname" v-model.trim="$v.nickname.$model"><br>
            <span class="error-text" v-if="$v.nickname.$dirty && !$v.nickname.required">Это поле обязательно для заполнения</span>
            <span class="error-text" v-if="$v.nickname.$dirty && !$v.nickname.validateNickname">Ник может содержать только латинские буквы, цифры и символы _ и -</span>
        </div>
        <span class="small-text">
            Все поля обязательны для заполнения<br>
            При предоставлении заведомо ложных данных в регистрации будет отказано<br>
            Нажимая "Подать заявку", ты даешь свое согласие на обработку и хранение персональных данных
        </span><br>
        <button :disabled="disabledButton" @click="submit()" class="button button-header not-selectable">Подать заявку</button><br>
        <div id="divider-end"></div>
    </div>
</template>

<script>
import { required, helpers } from 'vuelidate/lib/validators';

const validateNickname = helpers.regex('validate', /^[0-9a-zA-Z_-]+$/);

export default {
    data() {
        return {
            school: '',
            fullname: '',
            phone: '',
            email: '',
            group: '',
            nickname: '',
            loading: false
        }
    },
    computed: {
        disabledButton() {
            return this.$v.school.$invalid || this.$v.fullname.$invalid || this.$v.phone.$invalid || this.$v.email.$invalid || this.$v.group.$invalid || this.$v.nickname.$invalid || this.loading;
        },
        disabledFields() {
            return this.loading;
        }
    },
    validations: {
        school: {
            required
        },
        fullname: {
            required
        },
        phone: {
            required
        },
        email: {
            required
        },
        group: {
            required
        },
        nickname: {
            required, validateNickname
        }
    },
    methods: {
        submit() {
            const vm = this;
            const axios = require('axios');
            vm.loading = true;
            axios.post('https://srv1.kaletise.me/submit', {
                school: vm.school,
                fullname: vm.fullname,
                phone: vm.phone,
                email: vm.email,
                group: vm.group,
                nickname: vm.nickname
            }, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(function(response) {
                if (response.data.status == 1) {
                    vm.$root.status = 1;
                } else if (response.data.status == 0) {
                    vm.$root.status = 2;
                }
                vm.loading = false;
            }).catch(function() {
                vm.$root.status = 2;
                vm.loading = false;
            });
        }
    }
}
</script>

<style>
select {
    width: 75%;
    margin: 5px;
    padding-left: 10px;
    background-color: transparent;
    border-radius: 0;
    border: 2px solid #ffffff;
    color: #ffffff;
    height: 45px;
}

select option {
    color: #000000;
    font-size: 15px;
    font-family: Arial, sans-serif;
}

.button {
    border: 0;
    margin-top: 10px;
    margin-bottom: 7px;
}

.input-container {
    margin: 10px 0;
}

.small-text {
    font-size: 11px;
}

.button-header {
    padding: 15px 15px;
    font-size: 20px;
    color: #ffffff;
    box-shadow: inset 0 -4px rgba(0, 0, 0, .2), inset 0 4px hsla(0, 0%, 100%, .3), inset -4px 0 hsla(0, 0%, 100%, .3), inset 4px 0 rgba(0, 0, 0, .2);
    text-align: center;
    background: rgb(78, 125, 223);
    transition: 0.4s;
}

.button-header:hover {
    background: rgb(34, 84, 188);
    transition: 0.4s;
    transform: scale(1.05);
}

.button-header:disabled {
    background: #666666;
}

#divider-end {
    display: none;
    padding-top: 120px;
}

*:focus {
    outline: none;
}

input::placeholder {
    color: #aaaaaa;
}

input {
    width: 75%;
    margin: 5px;
    padding-left: 10px;
    background-color: transparent;
    border-radius: 0;
    border: 2px solid #ffffff;
    color: #ffffff;
    height: 45px;
}

input.error {
    border: 2px solid #ff9494 !important;
}

.error-text {
    font-size: 12px;
    color: #ff9494;
}

@media (max-width: 766px) {
    #divider {
        padding-top: 40px;
    }

    #divider-end {
        display: block;
    }

    select {
        width: 90%;
    }

    input {
        width: 90%;
    }
}

@media (max-height: 800px) {
    select {
        width: 90%;
    }

    input {
        width: 90%;
    }
}
</style>