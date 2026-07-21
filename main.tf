resource "local_file" "games" {
  filename = "/home/Satyaki/favorite-games"
  content  = "FIFA 21"
}

output "games" {
  value = local_file.games.content
}