movies = {
    :Titanic => 5
}

puts "What would you like to do?"
choice = gets.chomp


case choice

when "add"
    puts "Please enter a movie:"
    title = gets.chomp
    if movies[title.to_sym].nil?
        puts "Rating?"
        rating = gets.chomp
        movies[title.to_sym] = rating.to_i
        puts "Pair added"
    else
        puts "#{title} already exists."
    end     

when "update"
   puts "Gimme a movie title.."
   title = gets.chomp
   if movies[title.to_sym].nil?
       puts "Sorry, movie not in hash"
   else
       puts "New rating?"
       rating = gets.chomp
       movies[title.to_sym] = rating.to_i
   end
       
when "display"
    movies.each do |movies, rating|
        puts "#{movies}: #{rating}"
    end    
    
when "delete"
    puts "What movie do you want to delete?"
    title = gets.chomp
    if movies[title.to_sym].nil?
        puts "Sorry, movie not in hash!"
    else
        movies.delete(title.to_sym)
    end    
else
    puts "Error!"
    
end    