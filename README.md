# Preparation of the Vector Database

## Data
The ./data repository has all the scraped data formatted with field-consistently in json

## Vector-DB
The ./qdrant repository has the code for vectorizing the data and keep them in the vector database. The vector database contains over 20k products

## Key points
> We have used text-embedding-3-small model for generating text em,bedding
> We have used clip-ViT-B-32 model for image embedding
> One vector point contains multiple vector points (text and image) to increase robustness

## Integration of LLAVA
we have used LLAVA for generating description for products from the less developed marketplaces
