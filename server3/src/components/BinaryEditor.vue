<template>
  <div>
    <h1>Edit Binary Affirmation for ID: {{ affirmation._id }}</h1>

    <div>
      <label for="messageText">Message:</label>
      <textarea id="messageText" v-model="affirmation.text"></textarea>
    </div>

    <h2>GPT Extracted Affirmations:</h2>
    <table>
      <tbody>
        <tr v-for="(value, key, index) in affirmation.affirmations" :key="'gpt-' + index">
          <td><textarea v-model="affirmationKeys.gpt[index]" /></td>
          <td><textarea v-model="affirmation.affirmations[key]" /></td>
        </tr>
      </tbody>
    </table>

    <h2>Corrected Affirmations:</h2>
    <table>
      <tbody>
        <tr v-for="(value, key, index) in affirmation.affirmations_corrections" :key="'corrected-' + index">
          <td><textarea v-model="affirmationKeys.corrected[index]" /></td>
          <td><textarea v-model="affirmation.affirmations_corrections[key]" /></td>
        </tr>
      </tbody>
    </table>

    <div>
      <input type="checkbox" v-model="affirmation.to_use_a"> Use this affirmation
    </div>

    <button @click="saveChanges">Save</button>
    <button @click="$emit('backToLanding')">Back</button>
  </div>
</template>

<script>
export default {
  props: {
    affirmation: Object
  },
  data() {
    return {
      affirmationKeys: {
        gpt: Object.keys(this.affirmation.affirmations),
        corrected: Object.keys(this.affirmation.affirmations_corrections)
      }
    }
  },
  watch: {
    affirmation: {
      deep: true,
      handler(newAffirmation) {
        this.affirmationKeys.gpt       = Object.keys(newAffirmation.affirmations);
        this.affirmationKeys.corrected = Object.keys(newAffirmation.affirmations_corrections);
      }
    }
  },
  methods: {
  saveChanges() {
    // Convert arrays back to objects based on the modified keys
    this.affirmation.affirmations = this.affirmationKeys.gpt.reduce((acc, key, index) => {
      if (key.trim() !== "") {
        acc[key] = Object.values(this.affirmation.affirmations)[index];
      }
      return acc;
    }, {});
    this.affirmation.affirmations_corrections = this.affirmationKeys.corrected.reduce((acc, key, index) => {
      if (key.trim() !== "") {
        acc[key] = Object.values(this.affirmation.affirmations_corrections)[index];
      }
      return acc;
    }, {});

    const updateData = { ...this.affirmation };
    delete updateData._id;

    fetch(`http://localhost:3001/update/${this.affirmation._id}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updateData)
    })
    .then(res => res.json())
    .then(response => {
      if (response.success) {
        alert('Affirmation saved successfully!');
        this.$emit('saved');
      } else {
        alert('Error saving affirmation. Please try again.');
      }
    });
  }
}

};
</script>