<template>
    <footer class="footer social-media">
        <a href="https://strcol.edu.kz"><i class="las la-globe"></i></a>
        <a href="https://t.me/cyber_ksk"><i class="lab la-telegram"></i></a>
        <a href="https://vk.com/kostack"><i class="lab la-vk"></i></a>
        <a href="https://instagram.com/stroy_college"><i class="lab la-instagram"></i></a>
        <a href="https://facebook.com/stroycollege"><i class="lab la-facebook"></i></a>
        <a href="https://github.com/strcol"><i class="lab la-github"></i></a>
    </footer>
</template>

<style>
.footer {
    position: absolute;
    padding: 25px;
    width: 100%;
    text-align: right;
    user-select: none;
    -moz-user-select: none;
    -khtml-user-select: none;
    -webkit-user-select: none;
    -o-user-select: none;
}

.social-media {
    font-size: 32px;
    z-index: 9999;
}

.footer a {
    margin: 3px;
    color: #ffffff;
}

.footer a:hover {
    color: #cccccc !important;
}

@media (max-width: 766px) {
    .footer {
        align-self: flex-end !important;
    }
}
</style>