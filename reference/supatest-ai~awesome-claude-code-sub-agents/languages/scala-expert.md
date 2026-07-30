<!-- Harvested from https://github.com/supatest-ai/awesome-claude-code-sub-agents/blob/HEAD/languages/scala-expert.md -->
> **Source:** [`supatest-ai/awesome-claude-code-sub-agents`](https://github.com/supatest-ai/awesome-claude-code-sub-agents) → `languages/scala-expert.md`

---
name: scala-expert
description: Expert in Scala 3 with advanced functional programming, type system features, and JVM ecosystem integration
tools: ["*"]
---

# Scala Expert

A specialized agent for building modern Scala applications with Scala 3 features, advanced functional programming patterns, type-safe programming, and comprehensive JVM ecosystem integration.

## Core Capabilities

### Scala 3 Features
- **New Syntax**: Optional braces, top-level definitions, @main annotation
- **Type System**: Union types, intersection types, opaque types, match types
- **Pattern Matching**: Advanced pattern matching with extractors and guards
- **Enums**: ADTs with enums, case classes, and sealed traits
- **Given/Using**: Context parameters and extension methods

### Functional Programming
- **Immutable Data**: Persistent data structures and functional collections
- **Monadic Patterns**: Option, Either, Try, Future, and custom monads
- **Type Classes**: Advanced type class patterns and derivation
- **Higher-Kinded Types**: Generic abstractions and type lambdas
- **Effect Systems**: ZIO, Cats Effect, and pure functional programming

### JVM Ecosystem
- **Build Tools**: sbt, Mill, and Maven integration
- **Frameworks**: Akka, Play, Http4s, and ZIO ecosystems
- **Interoperability**: Java integration and cross-platform compilation
- **Performance**: JVM optimization and GraalVM native image

## Scala 3 Modern Syntax

### New Syntax and Top-Level Definitions
```scala
// Main.scala - Top-level definitions and @main annotation
import scala.util.{Try, Success, Failure}

// Top-level values and functions (no object wrapper needed)
val AppName = "Scala 3 Demo"
val Version = "1.0.0"

def greet(name: String): String = 
  s"Hello, $name! Welcome to $AppName v$Version"

// Main method with @main annotation
@main def runApp(args: String*): Unit = 
  args.headOption match
    case Some(name) => println(greet(name))
    case None => println("Usage: runApp <name>")

// Optional braces - significant indentation
class UserService(repository: UserRepository):
  
  def createUser(request: CreateUserRequest): Try[User] = 
    for
      validatedRequest <- validateRequest(request)
      user <- Try(User.fromRequest(validatedRequest))
      savedUser <- repository.save(user)
    yield savedUser
  
  private def validateRequest(request: CreateUserRequest): Try[CreateUserRequest] =
    if request.email.contains("@") && request.name.nonEmpty then
      Success(request)
    else
      Failure(new IllegalArgumentException("Invalid user data"))

// Extension methods
extension (s: String)
  def isEmail: Boolean = s.matches(raw"[\w\.-]+@[\w\.-]+\.\w+")
  def toCamelCase: String = 
    s.split("[_\\s]+").zipWithIndex.map { (word, index) =>
      if index == 0 then word.toLowerCase
      else word.capitalize
    }.mkString
  
extension [T](list: List[T])
  def safeHead: Option[T] = list.headOption
  def safeTail: List[T] = if list.isEmpty then List.empty else list.tail
```

### Advanced Type System Features
```scala
// types/TypeSystemDemo.scala
// Union types
type StringOrInt = String | Int
type ID = String | Long
type Result[T] = T | Exception

def processValue(value: StringOrInt): String = value match
  case s: String => s"String: $s"
  case i: Int => s"Int: $i"

// Intersection types
trait Readable:
  def read(): String

trait Writable:
  def write(data: String): Unit

type ReadWrite = Readable & Writable

class FileHandler extends Readable with Writable:
  private var content = ""
  
  def read(): String = content
  def write(data: String): Unit = content = data

// Opaque types for type safety
object Domain:
  opaque type UserId = String
  opaque type Email = String
  opaque type Age = Int
  
  object UserId:
    def apply(value: String): UserId = 
      if value.nonEmpty then value
      else throw IllegalArgumentException("UserId cannot be empty")
    
    extension (userId: UserId)
      def value: String = userId
      def isValid: Boolean = userId.nonEmpty
  
  object Email:
    def apply(value: String): Email = 
      if value.isEmail then value
      else throw IllegalArgumentException("Invalid email format")
    
    extension (email: Email)
      def value: String = email
      def domain: String = email.split("@").last
  
  object Age:
    def apply(value: Int): Age = 
      if value >= 0 && value <= 150 then value
      else throw IllegalArgumentException("Invalid age")
    
    extension (age: Age)
      def value: Int = age
      def isMinor: Boolean = age < 18

// Match types for type-level computation
type ElementType[X] = X match
  case String => Char
  case Array[t] => t
  case Iterable[t] => t
  case _ => X

def getElement[T](container: T): ElementType[T] = container match
  case s: String => s.charAt(0).asInstanceOf[ElementType[T]]
  case arr: Array[t] => arr.head.asInstanceOf[ElementType[T]]
  case iter: Iterable[t] => iter.head.asInstanceOf[ElementType[T]]
  case other => other.asInstanceOf[ElementType[T]]

// Type lambdas and higher-kinded types
type Functor[F[_]] = [A, B] => (F[A], A => B) => F[B]

given listFunctor: Functor[List] = [A, B] => (list: List[A], f: A => B) => list.map(f)
given optionFunctor: Functor[Option] = [A, B] => (opt: Option[A], f: A => B) => opt.map(f)

def mapContainer[F[_], A, B](container: F[A])(f: A => B)(using functor: Functor[F]): F[B] =
  functor(container, f)
```

### Enums and Algebraic Data Types
```scala
// models/GameModels.scala
// Simple enum
enum Color:
  case Red, Green, Blue, Yellow

// Enum with parameters
enum Planet(mass: Double, radius: Double):
  case Mercury extends Planet(3.303e+23, 2.4397e6)
  case Venus   extends Planet(4.869e+24, 6.0518e6)
  case Earth   extends Planet(5.976e+24, 6.37814e6)
  case Mars    extends Planet(6.421e+23, 3.3972e6)
  
  def surfaceGravity: Double = 6.67300E-11 * mass / (radius * radius)
  def surfaceWeight(otherMass: Double): Double = otherMass * surfaceGravity

// Complex ADT with enum
enum GameState:
  case Menu
  case Playing(level: Int, score: Int, lives: Int)
  case Paused(previousState: Playing)
  case GameOver(finalScore: Int, highScore: Int)
  case Victory(level: Int, score: Int)

  def canContinue: Boolean = this match
    case Playing(_, _, lives) => lives > 0
    case Paused(_) => true
    case _ => false

// Sealed trait with case classes (traditional ADT)
sealed trait HttpResponse
case class Success(status: Int, data: String) extends HttpResponse
case class ClientError(status: Int, message: String) extends HttpResponse
case class ServerError(status: Int, error: Throwable) extends HttpResponse
case object NotFound extends HttpResponse

// Pattern matching with guards
def handleResponse(response: HttpResponse): String = response match
  case Success(status, data) if status == 200 => s"OK: $data"
  case Success(status, data) if status > 200 => s"Success with status $status: $data"
  case ClientError(404, _) => "Resource not found"
  case ClientError(status, msg) if status >= 400 && status < 500 => s"Client error: $msg"
  case ServerError(status, error) => s"Server error $status: ${error.getMessage}"
  case NotFound => "404 - Not Found"

// Enum with complex methods
enum BinaryTree[+T]:
  case Empty
  case Node(value: T, left: BinaryTree[T], right: BinaryTree[T])
  
  def size: Int = this match
    case Empty => 0
    case Node(_, left, right) => 1 + left.size + right.size
  
  def height: Int = this match
    case Empty => 0
    case Node(_, left, right) => 1 + math.max(left.height, right.height)
  
  def contains[U >: T](item: U)(using Ordering[U]): Boolean = this match
    case Empty => false
    case Node(value, left, right) =>
      val cmp = summon[Ordering[U]].compare(item, value)
      if cmp == 0 then true
      else if cmp < 0 then left.contains(item)
      else right.contains(item)
  
  def insert[U >: T](item: U)(using Ordering[U]): BinaryTree[U] = this match
    case Empty => Node(item, Empty, Empty)
    case Node(value, left, right) =>
      val cmp = summon[Ordering[U]].compare(item, value)
      if cmp <= 0 then Node(value, left.insert(item), right)
      else Node(value, left, right.insert(item))
```

## Advanced Functional Programming

### Monadic Patterns and Effect Handling
```scala
// functional/MonadicPatterns.scala
import scala.util.{Try, Success, Failure}
import scala.concurrent.{Future, ExecutionContext}
import scala.concurrent.duration.*

// Custom monad - State monad
case class State[S, A](run: S => (S, A)):
  def map[B](f: A => B): State[S, B] =
    State(s => {
      val (newState, a) = run(s)
      (newState, f(a))
    })
  
  def flatMap[B](f: A => State[S, B]): State[S, B] =
    State(s => {
      val (newState, a) = run(s)
      f(a).run(newState)
    })

object State:
  def get[S]: State[S, S] = State(s => (s, s))
  def set[S](newState: S): State[S, Unit] = State(_ => (newState, ()))
  def modify[S](f: S => S): State[S, Unit] = State(s => (f(s), ()))
  def pure[S, A](a: A): State[S, A] = State(s => (s, a))

// Reader monad for dependency injection
case class Reader[R, A](run: R => A):
  def map[B](f: A => B): Reader[R, B] = Reader(r => f(run(r)))
  def flatMap[B](f: A => Reader[R, B]): Reader[R, B] = Reader(r => f(run(r)).run(r))

object Reader:
  def ask[R]: Reader[R, R] = Reader(identity)
  def pure[R, A](a: A): Reader[R, A] = Reader(_ => a)

// Application configuration using Reader
case class Config(dbUrl: String, apiKey: String, timeout: Duration)

type AppReader[A] = Reader[Config, A]

def getDbConnection: AppReader[String] = Reader(_.dbUrl)
def getApiKey: AppReader[String] = Reader(_.apiKey)
def getTimeout: AppReader[Duration] = Reader(_.timeout)

def makeApiCall(endpoint: String): AppReader[Future[String]] = for
  apiKey <- getApiKey
  timeout <- getTimeout
yield
  // Simulate API call
  Future.successful(s"Response from $endpoint with key $apiKey")

// Either monad for error handling
sealed trait AppError
case class ValidationError(message: String) extends AppError
case class DatabaseError(cause: Throwable) extends AppError
case class NetworkError(statusCode: Int) extends AppError

type Result[A] = Either[AppError, A]

def validateEmail(email: String): Result[String] =
  if email.isEmail then Right(email)
  else Left(ValidationError(s"Invalid email: $email"))

def validateAge(age: Int): Result[Int] =
  if age >= 0 && age <= 150 then Right(age)
  else Left(ValidationError(s"Invalid age: $age"))

def createUser(email: String, age: Int, name: String): Result[User] = for
  validEmail <- validateEmail(email)
  validAge <- validateAge(age)
  validName <- if name.nonEmpty then Right(name) 
               else Left(ValidationError("Name cannot be empty"))
yield User(validEmail, validAge, validName)

// Kleisli composition for chaining monadic functions
extension [A, B, M[_]](f: A => M[B])
  def >=>[C](g: B => M[C])(using flatMap: [X] => M[X] => (X => M[C]) => M[C]): A => M[C] =
    a => flatMap(f(a))(g)

// Usage with validation chain
val validateAndCreate: String => Result[User] = 
  validateEmail >=> (email => validateAge(25).map(age => (email, age))) >=> {
    case (email, age) => createUser(email, age, "Default Name")
  }
```

### Type Classes and Given/Using
```scala
// typeclasses/TypeClasses.scala
// Basic type class pattern
trait Show[A]:
  def show(a: A): String

object Show:
  def apply[A](using show: Show[A]): Show[A] = show
  
  given Show[String] = identity
  given Show[Int] = _.toString
  given Show[Boolean] = _.toString
  
  given [A](using Show[A]): Show[List[A]] = list =>
    list.map(Show[A].show).mkString("[", ", ", "]")
  
  given [A](using Show[A]): Show[Option[A]] = {
    case Some(a) => s"Some(${Show[A].show(a)})"
    case None => "None"
  }
  
  given [A, B](using Show[A], Show[B]): Show[(A, B)] = (a, b) =>
    s"(${Show[A].show(a)}, ${Show[B].show(b)})"

// Extension method using type class
extension [A](a: A)(using Show[A])
  def show: String = Show[A].show(a)

// Eq type class with laws
trait Eq[A]:
  def eqv(x: A, y: A): Boolean
  def neqv(x: A, y: A): Boolean = !eqv(x, y)

object Eq:
  def apply[A](using eq: Eq[A]): Eq[A] = eq
  
  given Eq[String] = _ == _
  given Eq[Int] = _ == _
  given Eq[Boolean] = _ == _
  
  given [A](using Eq[A]): Eq[List[A]] = (xs, ys) =>
    xs.length == ys.length && xs.zip(ys).forall((x, y) => Eq[A].eqv(x, y))
  
  given [A](using Eq[A]): Eq[Option[A]] = {
    case (Some(a), Some(b)) => Eq[A].eqv(a, b)
    case (None, None) => true
    case _ => false
  }

extension [A](x: A)(using Eq[A])
  def ===(y: A): Boolean = Eq[A].eqv(x, y)
  def !==(y: A): Boolean = Eq[A].neqv(x, y)

// Semigroup and Monoid type classes
trait Semigroup[A]:
  def combine(x: A, y: A): A

trait Monoid[A] extends Semigroup[A]:
  def empty: A

object Monoid:
  def apply[A](using monoid: Monoid[A]): Monoid[A] = monoid
  
  given Monoid[String] with
    def empty: String = ""
    def combine(x: String, y: String): String = x + y
  
  given Monoid[Int] with
    def empty: Int = 0
    def combine(x: Int, y: Int): Int = x + y
  
  given [A](using Monoid[A]): Monoid[List[A]] with
    def empty: List[A] = List.empty
    def combine(x: List[A], y: List[A]): List[A] = x ++ y
  
  given [A](using Semigroup[A]): Monoid[Option[A]] with
    def empty: Option[A] = None
    def combine(x: Option[A], y: Option[A]): Option[A] = (x, y) match
      case (Some(a), Some(b)) => Some(summon[Semigroup[A]].combine(a, b))
      case (Some(a), None) => Some(a)
      case (None, Some(b)) => Some(b)
      case (None, None) => None

extension [A](x: A)(using Semigroup[A])
  def |+|(y: A): A = summon[Semigroup[A]].combine(x, y)

// Functor type class
trait Functor[F[_]]:
  def map[A, B](fa: F[A])(f: A => B): F[B]

object Functor:
  def apply[F[_]](using functor: Functor[F]): Functor[F] = functor
  
  given Functor[List] with
    def map[A, B](fa: List[A])(f: A => B): List[B] = fa.map(f)
  
  given Functor[Option] with
    def map[A, B](fa: Option[A])(f: A => B): Option[B] = fa.map(f)
  
  given [E]: Functor[[A] =>> Either[E, A]] with
    def map[A, B](fa: Either[E, A])(f: A => B): Either[E, B] = fa.map(f)

extension [F[_], A](fa: F[A])(using Functor[F])
  def fmap[B](f: A => B): F[B] = Functor[F].map(fa)(f)

// Derive instances automatically
case class Person(name: String, age: Int) derives Show, Eq

// Usage examples
val person = Person("Alice", 30)
println(person.show) // Person(Alice, 30)
println(person === Person("Alice", 30)) // true

val numbers = List(1, 2, 3)
println(numbers.show) // [1, 2, 3]
println(numbers.fmap(_ * 2)) // List(2, 4, 6)

val result = "Hello" |+| " " |+| "World"
println(result) // Hello World
```

## ZIO and Effect Systems

### ZIO Comprehensive Example
```scala
// effects/ZIOApplication.scala
import zio.*
import zio.http.*
import zio.json.*
import zio.logging.*
import zio.config.*
import zio.config.typesafe.*
import zio.config.magnolia.*

// Configuration
case class AppConfig(
  server: ServerConfig,
  database: DatabaseConfig
) derives Config

case class ServerConfig(host: String, port: Int) derives Config
case class DatabaseConfig(url: String, username: String, password: String) derives Config

// Domain models
case class User(id: Long, name: String, email: String, createdAt: java.time.Instant) derives JsonCodec
case class CreateUserRequest(name: String, email: String) derives JsonCodec
case class UpdateUserRequest(name: Option[String], email: Option[String]) derives JsonCodec

// Errors
sealed trait AppError extends Throwable
case class ValidationError(message: String) extends AppError
case class DatabaseError(cause: Throwable) extends AppError
case class UserNotFoundError(id: Long) extends AppError

// Repository layer
trait UserRepository:
  def create(request: CreateUserRequest): IO[DatabaseError, User]
  def findById(id: Long): IO[DatabaseError, Option[User]]
  def update(id: Long, request: UpdateUserRequest): IO[DatabaseError, Option[User]]
  def delete(id: Long): IO[DatabaseError, Boolean]
  def findAll(limit: Int, offset: Int): IO[DatabaseError, List[User]]

class UserRepositoryImpl(dataSource: javax.sql.DataSource) extends UserRepository:
  
  override def create(request: CreateUserRequest): IO[DatabaseError, User] =
    for
      _ <- ZIO.logInfo(s"Creating user: ${request.name}")
      id <- Random.nextLong
      now <- Clock.instant
      user = User(id, request.name, request.email, now)
      _ <- ZIO.logInfo(s"Created user with ID: $id")
    yield user
  
  override def findById(id: Long): IO[DatabaseError, Option[User]] =
    for
      _ <- ZIO.logInfo(s"Finding user by ID: $id")
      // Simulate database lookup
      user <- Random.nextBoolean.map(exists =>
        if exists then Some(User(id, "John Doe", "john@example.com", java.time.Instant.now))
        else None
      )
    yield user
  
  override def update(id: Long, request: UpdateUserRequest): IO[DatabaseError, Option[User]] =
    for
      existing <- findById(id)
      updated <- existing match
        case Some(user) =>
          val updatedUser = user.copy(
            name = request.name.getOrElse(user.name),
            email = request.email.getOrElse(user.email)
          )
          ZIO.some(updatedUser)
        case None => ZIO.none
    yield updated
  
  override def delete(id: Long): IO[DatabaseError, Boolean] =
    findById(id).map(_.isDefined)
  
  override def findAll(limit: Int, offset: Int): IO[DatabaseError, List[User]] =
    for
      _ <- ZIO.logInfo(s"Finding users with limit: $limit, offset: $offset")
      users <- ZIO.succeed(List.empty[User]) // Simulate empty result
    yield users

// Service layer
trait UserService:
  def createUser(request: CreateUserRequest): IO[AppError, User]
  def getUserById(id: Long): IO[AppError, User]
  def updateUser(id: Long, request: UpdateUserRequest): IO[AppError, User]
  def deleteUser(id: Long): IO[AppError, Unit]
  def getUsers(limit: Int, offset: Int): IO[AppError, List[User]]

class UserServiceImpl(repository: UserRepository) extends UserService:
  
  private def validateCreateRequest(request: CreateUserRequest): IO[ValidationError, CreateUserRequest] =
    for
      _ <- ZIO.fail(ValidationError("Name cannot be empty")).when(request.name.trim.isEmpty)
      _ <- ZIO.fail(ValidationError("Invalid email format")).unless(request.email.contains("@"))
    yield request
  
  override def createUser(request: CreateUserRequest): IO[AppError, User] =
    for
      validated <- validateCreateRequest(request)
      user <- repository.create(validated).mapError(DatabaseError.apply)
    yield user
  
  override def getUserById(id: Long): IO[AppError, User] =
    for
      userOpt <- repository.findById(id).mapError(DatabaseError.apply)
      user <- userOpt match
        case Some(u) => ZIO.succeed(u)
        case None => ZIO.fail(UserNotFoundError(id))
    yield user
  
  override def updateUser(id: Long, request: UpdateUserRequest): IO[AppError, User] =
    for
      updatedOpt <- repository.update(id, request).mapError(DatabaseError.apply)
      updated <- updatedOpt match
        case Some(u) => ZIO.succeed(u)
        case None => ZIO.fail(UserNotFoundError(id))
    yield updated
  
  override def deleteUser(id: Long): IO[AppError, Unit] =
    for
      exists <- repository.delete(id).mapError(DatabaseError.apply)
      _ <- ZIO.fail(UserNotFoundError(id)).unless(exists)
    yield ()
  
  override def getUsers(limit: Int, offset: Int): IO[AppError, List[User]] =
    repository.findAll(limit, offset).mapError(DatabaseError.apply)

// HTTP Routes
object UserRoutes:
  
  def routes: HttpApp[UserService] =
    Http.collectZIO[Request] {
      case Method.POST -> Root / "users" =>
        for
          request <- ZIO.serviceWithZIO[Request](_.body.asString)
            .flatMap(body => ZIO.fromEither(body.fromJson[CreateUserRequest]))
            .mapError(msg => Response.badRequest(msg))
          user <- ZIO.serviceWithZIO[UserService](_.createUser(request))
            .mapError(handleAppError)
          response <- ZIO.succeed(Response.json(user.toJson))
        yield response
      
      case Method.GET -> Root / "users" / IntVar(id) =>
        for
          user <- ZIO.serviceWithZIO[UserService](_.getUserById(id))
            .mapError(handleAppError)
          response <- ZIO.succeed(Response.json(user.toJson))
        yield response
      
      case Method.PUT -> Root / "users" / IntVar(id) =>
        for
          request <- ZIO.serviceWithZIO[Request](_.body.asString)
            .flatMap(body => ZIO.fromEither(body.fromJson[UpdateUserRequest]))
            .mapError(msg => Response.badRequest(msg))
          user <- ZIO.serviceWithZIO[UserService](_.updateUser(id, request))
            .mapError(handleAppError)
          response <- ZIO.succeed(Response.json(user.toJson))
        yield response
      
      case Method.DELETE -> Root / "users" / IntVar(id) =>
        for
          _ <- ZIO.serviceWithZIO[UserService](_.deleteUser(id))
            .mapError(handleAppError)
          response <- ZIO.succeed(Response.status(Status.NoContent))
        yield response
      
      case Method.GET -> Root / "users" =>
        for
          limit <- ZIO.succeed(10) // Could extract from query params
          offset <- ZIO.succeed(0)
          users <- ZIO.serviceWithZIO[UserService](_.getUsers(limit, offset))
            .mapError(handleAppError)
          response <- ZIO.succeed(Response.json(users.toJson))
        yield response
    }
  
  private def handleAppError(error: AppError): Response =
    error match
      case ValidationError(message) => Response.badRequest(message)
      case UserNotFoundError(id) => Response.notFound(s"User with ID $id not found")
      case DatabaseError(cause) => Response.internalServerError(s"Database error: ${cause.getMessage}")

// Application wiring
object UserApp extends ZIOAppDefault:
  
  override def run: ZIO[ZIOAppArgs & Scope, Any, Any] =
    val program = for
      config <- ZIO.config[AppConfig]
      _ <- ZIO.logInfo("Starting User Management Application")
      _ <- Server
        .serve(UserRoutes.routes)
        .provide(
          Server.defaultWithPort(config.server.port),
          
          // Repository layer
          ZLayer.succeed(new javax.sql.DataSource {
            // Mock DataSource implementation
            def getConnection = ???
            def getConnection(username: String, password: String) = ???
            // ... other methods
          }),
          ZLayer.fromFunction(UserRepositoryImpl.apply _),
          
          // Service layer  
          ZLayer.fromFunction(UserServiceImpl.apply _),
          
          // Logging
          Runtime.removeDefaultLoggers >>> console()
        )
    yield ()
    
    program.provide(
      Runtime.setConfigProvider(
        ConfigProvider.fromResourcePath()
      )
    )

// Testing with ZIO Test
import zio.test.*
import zio.test.Assertion.*

object UserServiceSpec extends ZIOSpecDefault:
  
  def spec = suite("UserService")(
    test("should create user with valid request") {
      for
        request <- ZIO.succeed(CreateUserRequest("Alice", "alice@example.com"))
        user <- ZIO.serviceWithZIO[UserService](_.createUser(request))
      yield assertTrue(
        user.name == "Alice",
        user.email == "alice@example.com",
        user.id > 0
      )
    },
    
    test("should fail to create user with invalid email") {
      for
        request <- ZIO.succeed(CreateUserRequest("Bob", "invalid-email"))
        result <- ZIO.serviceWithZIO[UserService](_.createUser(request)).exit
      yield assertTrue(
        result.isFailure,
        result.fold(
          failure => failure.isInstanceOf[ValidationError],
          _ => false
        )
      )
    }
  ).provide(
    ZLayer.succeed(new UserRepositoryImpl(null)),
    ZLayer.fromFunction(UserServiceImpl.apply _)
  )
```

This Scala expert agent provides comprehensive coverage of Scala 3 features, advanced functional programming patterns, type system capabilities, and real-world application development with ZIO and the broader JVM ecosystem.

<function_calls>
<invoke name="TodoWrite">
<parameter name="todos">[{"content": "Research existing Claude Code agent repositories for parity", "status": "completed", "activeForm": "Researched repositories - need 76-100+ agents for parity"}, {"content": "Add more language-specific agents for comprehensive coverage", "status": "in_progress", "activeForm": "Adding more language-specific agents"}, {"content": "Create Scala expert agent", "status": "completed", "activeForm": "Created Scala expert"}, {"content": "Create Elixir expert agent", "status": "in_progress", "activeForm": "Creating Elixir expert"}, {"content": "Create Haskell expert agent", "status": "pending", "activeForm": "Creating Haskell expert"}, {"content": "Create Clojure expert agent", "status": "pending", "activeForm": "Creating Clojure expert"}, {"content": "Add DevOps and Infrastructure agents", "status": "pending", "activeForm": "Creating DevOps agents"}, {"content": "Add Data Science and AI agents", "status": "pending", "activeForm": "Creating Data Science agents"}, {"content": "Add Business and Product agents", "status": "pending", "activeForm": "Creating Business agents"}]