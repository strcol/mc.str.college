<template>
    <div class="centerize" id="success">
        <i class="las la-check-circle minecraft-green"></i><br><br>
        <h3>Заявка отправлена</h3>
        Заявка на участие в мероприятии отправлена!
    </div>
</template>

<style>
.centerize {
    margin: 0 auto;
    text-align: center;
}

.la-check-circle {
    font-size: 144px;
}

.minecraft-green {
    color: rgb(0, 170, 0);
}

#success a {
    color: #bbbbbb;
}

#success a:hover {
    color: #dddddd;
    text-decoration: none;
}

@media (max-width: 766px) {
    .la-check-circle {
        font-size: 72px;
    }
}
</style>