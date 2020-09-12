function checkPage(pageName)
{
    if (pageName === 'Main')
    {
        document.getElementById('main-page-nav').classList.add('active');
    }
    else if (pageName === 'Movie_Research')
    {
        document.getElementById('movieresearch-page-nav').classList.add('active');
    }
    else if (pageName === 'Review_List')
    {
        document.getElementById('reviewlist-page-nav').classList.add('active');
    }
    else if (pageName === 'Review_Write')
    {
        document.getElementById('reviewwrite-page-nav').classList.add('active');
    }
    else if (pageName === 'Wishlist')
    {
        document.getElementById('wishlist-page-nav').classList.add('active');
    }
}