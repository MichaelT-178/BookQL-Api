# BookQL Api
# [Api Landing Page](https://api.bookql.com/)
## [Link to BookQL Website](https://michaelt-w23.github.io/bookql-website/add-author)
This is the GraphQL api I made for the [BookQL](https://www.target.com/) website.

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
https://api.bookql.com/graphql
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
To make a request to this API using Postman, use the following link.
You'll use a POST request for both queries and mutations. Go to Body -> GraphQL and paste in your query.
```
https://api.bookql.com/grapqhl
```

# Attribution
favicon by https://www.flaticon.com/authors/popo2021