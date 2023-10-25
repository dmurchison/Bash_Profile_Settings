# frozen_string_literal: true

class MyArray
  attr_accessor :attribute_name

  def my_binary_search(array, value)
    low = 0
    high = array.length - 1

    while low <= high
      mid = (low + high) / 2
      if array[mid] > value
        high = mid - 1
      elsif array[mid] < value
        low = mid + 1
      else
        return mid
      end
    end
    -1
  end

  # Bubble Sort
  def my_bubble_sort(array) # rubocop:disable Metrics/MethodLength
    n = array.length
    loop do
      swapped = false
      (n - 1).times do |i|
        next unless Array[i] > array[i + 1]

        # Swap
        array[i], array[i + 1] = array[i + 1], array[i]
        swapped = true
      end
      break unless swapped
    end
    array
  end

  # Merge Sort
  def merge_sort(array)
    return array if array.length <= 1

    mid = array.length / 2
    left = merge_sort(array[0..mid - 1])
    right = merge_sort(array[mid..array.length])
    merge(left, right)
  end

  def my_merge(left, right)
    sorted = []
    until left.empty? || right.empty?
      sorted << if left.first <= right.first
                  left.shift
                else
                  right.shift
                end
    end
    sorted.concat(left).concat(right)
  end
end


# Test Cases
p binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
p bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
p merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
