<template>
  <div>
    <h1>Edit Data for ID: {{ record._id }}</h1>

    <table>
      <thead>
        <tr>
          <th>Characteristics</th>
          <th>Score</th>
          <th>Corrected Score</th>
          <th>Explanation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(char, index) in characteristics" :key="char._id">
          <td>{{ char.str }}</td>
          <td><input type="number" v-model="record.score_list[index]" /></td>
          <td><input type="number" v-model="record.score_list_corrections[index]" /></td>
          <td><input v-model="record.score_list_explanations[char.str]" /></td>
        </tr>
      </tbody>
    </table>

    <h2>Usage:</h2>
    <input type="checkbox" v-model="record.to_use_c"> Use this record

    <br><br>
    <button @click="saveChanges">Save</button>
    <button @click="$emit('cancel')">Cancel</button>
  </div>
</template>


<script>
export default {
  props: {
    record: Object
  },
  data() {
    return {
      characteristics: []
    };
  },
  methods: {
    saveChanges() {
        const updateData = { ...this.record };
        delete updateData._id; // Remove the _id field from the data to be sent

        fetch(`http://localhost:3001/update/${this.record._id}`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(updateData)
        })
        .then(res => res.json())
        .then(response => {
            if (response.success) {
            alert('Data saved successfully!');
            this.$emit('saved'); // Notify the parent component
            } else {
            alert('Error saving data. Please try again.');
            }
        });
    }

  },
  mounted() {
    fetch('http://localhost:3001/characteristics')
      .then(response => response.json())
      .then(data => {
        this.characteristics = data;
        console.log(data)
      });
  },
};
</script>