from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import TodoItems
from .serializers import TodoSerializers
from rest_framework import serializers
from rest_framework import status

# API Overview endpoint
@api_view(['GET'])
def ApiOverview(request):
    # Dictionary of available API endpoints and their URLs
	api_urls = {
        'all_items': '/',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)


# View all todo items endpoint
@api_view(['GET'])
def view_items(request):
    # Checking for query parameters from the URL
	if request.query_params:
        # Filtering TodoItems queryset based on the query parameters
		items = TodoItems.objects.filter(**request.query_params.dict())
	else:
        # If no query parameters, retrieve all TodoItems
		items = TodoItems.objects.all()

	# If there are items in the queryset
	if items:
        # Serialize the queryset using TodoSerializers
		serializer = TodoSerializers(items, many=True)
		return Response(serializer.data)
	else:
        # If no items found, return a 404 status code
		return Response(status=status.HTTP_404_NOT_FOUND)


# Add a new todo item endpoint
@api_view(['POST'])
def add_items(request):
    # Serialize the request data using TodoSerializers
	item = TodoSerializers(data=request.data)

	if item.is_valid():
        # If the serialized data is valid, save the item and return the serialized data
		item.save()
		return Response(item.data)
	else:
        # If the serialized data is not valid, return a 404 status code
		return Response(status=status.HTTP_404_NOT_FOUND)


# Update an existing todo item endpoint
@api_view(['POST'])
def update_items(request, pk):
    # Retrieve the todo item with the specified pk (primary key)
	item = TodoItems.objects.get(pk=pk)
	# Serialize the instance and update it with the request data
	data = TodoSerializers(instance=item, data=request.data)

	if data.is_valid():
        # If the serialized data is valid, save the updated item and return the serialized data
		data.save()
		return Response(data.data)
	else:
        # If the serialized data is not valid or the item does not exist, return a 404 status code
		return Response(status=status.HTTP_404_NOT_FOUND)


# Delete a todo item endpoint
@api_view(['DELETE'])
def delete_items(request, pk):
    # Retrieve the todo item with the specified pk (primary key) or return a 404 error
    item = get_object_or_404(TodoItems, pk=pk)
    # Delete the item
    item.delete()
    # Return a 202 status code to indicate successful deletion
    return Response(status=status.HTTP_202_ACCEPTED)
