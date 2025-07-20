# BookQL Api
# [Api Landing Page](https://bookql.com/)
This is the GraphQL api I made for the [BookQL](https://github.com/MichaelT-W23/bookql-website) website.

## BookQL Website
- ### [Link to React Website](https://michaelt-w23.github.io/react-graphql/)
- ### [Link to Vue Website](https://michaelt-w23.github.io/bookql-website/)

## Backup 
If the Api Landing Page is being blocked by Cisco Umbrella, try this [link](https://bookql-api-mcp6.onrender.com/) instead. It's the same as the other one, just without the domain name.

## Technologies Used
- GraphQL
- Python
- FastAPI
- Strawberry
- SQLite3
- Petite-Vue (Landing Page)
- Render 
- Cloudflare

## How to Query the Api
Open the following Link in your browser.
```
https://bookql.com/graphql
```

# Queries

Get All Authors
```
query {
  getAllAuthors {
      id
      name
      age
      nationality
      books {
        id
        title
        publicationYear
        genre
      }
  }
}
```

Get All Books
```
query {
  getAllBooks {
      id
      title
      publicationYear
      genre
      author {
        id
        name
        age
        nationality
      }
  }
}
```

Get Author by ID
```
query {
  getAuthor(id: 1) {
      id
      name
      age
      nationality
      books {
        id
        title
        publicationYear
        genre
      }
  }
}
```

Get Book By ID
```
query {
  getBook(id: 1) {
      id
      title
      publicationYear
      genre
      author {
        id
        name
        age
        nationality
      }
  }
}
```

Get All Genres
```
query {
  getAllGenres
}
```

Get Book By Genre
```
query {
  getBooksByGenre(genre: "Fantasy") {
      id
      title
      publicationYear
      genre
      author {
        id
        name
        age
        nationality
      }
  }
}
```

# Mutations 

Create Author 

```
mutation {
    createAuthor(name: "Alice", age: 29, nationality: "British") {
        id
        name
        age
        nationality
    }
}
```

Create Book

```
mutation {
    createBook(
        title: "Lord of the Rings", 
        publicationYear: 1954, 
        genre: "fantasy", 
        authorId: 2
    ) {
        id
        title
        publicationYear
        genre
        author {
          id
          name
          age
          nationality
        }
    }
}
```

Delete Author By ID

```
mutation {
    deleteAuthor(authorId: 1)
}
```

Delete Book By ID
```
mutation {
    deleteBook(bookId: 1)
}
```

# Make a Postman Request

1. Make a **POST** request to the following link for both queries and mutations.

2. Configure the Request Body
   - Go to the **Body** tab.
   - Select **GraphQL**.
   - Paste your query into the field.

```
https://bookql.com/grapqhl
```

If Cisco Umbrella is blocking the link above, use this one instead.
```
https://bookql-api-mcp6.onrender.com/graphql
```

# Attribution
favicon by https://www.flaticon.com/authors/popo2021

