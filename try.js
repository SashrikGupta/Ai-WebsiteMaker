


async function give_image_by_title(title)
{
     title = title.replace(/ /g, '+') ;
     const response =  await fetch(`https://api.unsplash.com/search/photos?page=1&query=${title}&client_id=J3Af0qhs3oT2DAqbTjP9IAwgM575BYNOrJlAcC-BtZs`)
     const data = await response.json()
     return data.results[0].urls.raw
}

const data = await give_image_by_title("night city")