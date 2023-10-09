CREATE TABLE "Like" (
  "id" UUID PRIMARY KEY,
  "user_id" UUID,
  "post_id" UUID,
  "date_added" DateTime
);

CREATE TABLE "UserPost" (
  "id" UUID PRIMARY KEY,
  "user_id" UUID,
  "title" Char(100),
  "game_link" URL(60),
  "body" Text,
  "date_added" DateTime
);

CREATE TABLE "UserPostImage" (
  "id" id PRIMARY KEY,
  "post_id" UUID,
  "image" ProcessedImage
);

CREATE TABLE "Message" (
  "id" UUID PRIMARY KEY,
  "room_id" UUID,
  "user_id" UUID,
  "content" Text,
  "date_added" DateTime
);

CREATE TABLE "Room" (
  "id" UUID PRIMARY KEY,
  "name" Char(30) UNIQUE,
  "slug" Slug UNIQUE,
  "premium" Boolean DEFAULT false,
  "date_added" DateTime
);

CREATE TABLE "User" (
  "id" UUID PRIMARY KEY,
  "first_name" Char(150),
  "last_name" Char(150),
  "username" Char(30) UNIQUE,
  "bio" Text,
  "photo" Image,
  "telegram_id" Char(30),
  "chess_profile_url" URL(60),
  "subscriber" Boolean DEFAULT false,
  "date_added" DateTime
);

CREATE TABLE "Discussion" (
  "id" UUID PRIMARY KEY,
  "title" Char(255),
  "text" Text,
  "author_id" UUID,
  "image" Image,
  "closed" Boolean DEFAULT false,
  "date_added" DateTime
);

CREATE TABLE "ReplyLike" (
  "id" UUID PRIMARY KEY,
  "reply_id" UUID,
  "user_id" UUID,
  "date_added" DateTime
);

CREATE TABLE "Reply" (
  "id" UUID PRIMARY KEY,
  "discussion_id" UUID,
  "text" Text,
  "author_id" UUID,
  "image" Image,
  "date_added" DateTime
);

CREATE UNIQUE INDEX ON "Like" ("user_id", "post_id");

ALTER TABLE "Like" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Like" ADD FOREIGN KEY ("post_id") REFERENCES "UserPost" ("id");

ALTER TABLE "UserPost" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "UserPostImage" ADD FOREIGN KEY ("post_id") REFERENCES "UserPost" ("id");

ALTER TABLE "Message" ADD FOREIGN KEY ("room_id") REFERENCES "Room" ("id");

ALTER TABLE "Message" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Discussion" ADD FOREIGN KEY ("author_id") REFERENCES "User" ("id");

ALTER TABLE "ReplyLike" ADD FOREIGN KEY ("reply_id") REFERENCES "Reply" ("id");

ALTER TABLE "ReplyLike" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Reply" ADD FOREIGN KEY ("discussion_id") REFERENCES "Discussion" ("id");

ALTER TABLE "Reply" ADD FOREIGN KEY ("author_id") REFERENCES "User" ("id");
