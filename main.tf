resource "local_file" "games" {
  filename = "/home/Satyaki/favorite-games"
  content  = "EFOOTBALL 27"
}

output "games" {
  value = local_file.games.content
}