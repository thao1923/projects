package main

import (
	"fmt"
)

// You create structs out of function
// Create a struct called AlbumSales with
// Name string
// Qty int

type AlbumSales struct {
	//Fill in the variables
	Name string
	Qty int
}

func main() {
	// I am interested to know the album sales of the Reputation album,
	// can you find it out online and round it to the 
	// nearest whole number and store that result in a struct and print it out?
	
	// Your code here
	fmt.Println(AlbumSales{"Reputation", 4500000})

	var sale *AlbumSales // specify the type of the variable
	sale = &AlbumSales{} // pointer points to the memory with the struct
	sale.Name = "Reputaion"
	sale.Qty = 1000
	fmt.Println(sale.Name, sale.Qty)

}