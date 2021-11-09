package com.allaboutscala.chapter.one.tutorial_06

object HelloWorldWithArguments extends App {
  println("Hello World With Arguments Scala Application!")
  println("Command Line Arguments Are:")
  println(args.mkString(", "))
}