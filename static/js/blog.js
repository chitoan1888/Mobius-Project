const onCopyBlogLink = (blogId) => {
    const blogEl = document.getElementsByClassName(blogId)
    const blogLink = blogEl[0].querySelector('.blog__btn').href
    navigator.clipboard.writeText(blogLink);
}