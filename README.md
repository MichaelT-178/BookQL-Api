# BookQL Api
# [Api Landing Page](https://bookql.com/)
This is the GraphQL api I made for the [BookQL](https://vue.bookql.com/) website. 

Note: The version of this API that's currently being hosted is built with Flask and is a slightly updated version of this one. The FastAPI version in this repo isn't deployed anywhere.

## BookQL Website
- ### [Link to React Website](https://react.bookql.com/)
- ### [Link to Vue Website](https://vue.bookql.com/)

## Technologies Used
- GraphQL
- Python
- FastAPI
- Strawberry
- SQLite3
- Petite-Vue (Landing Page)
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

# Attribution
favicon by https://www.flaticon.com/authors/popo2021

