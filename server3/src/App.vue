<!-- App.vue -->

<template>
  <div id="app">
    <LandingPage v-if="currentView === 'landing'" @changeRoute="setCurrentView" />
    <div v-if="currentView === 'recordEditor'">
      <div v-if="currentRecord">
        <DataEditor :record="currentRecord" @saved="onSaved" />
      </div>
      <div v-else>
        <ul>
          <li v-for="record in messages" :key="record._id" @click="editRecord(record)">
            {{ record.text }}
          </li>
        </ul>
      </div>
    </div>
    <div v-if="currentView === 'binaryEditor'">
      <div v-if="currentAffirmation">
        <BinaryEditor :affirmation="currentAffirmation" @saved="onSaved" />
      </div>
      <div v-else>
        <ul>
          <li v-for="affirmation in messages" :key="affirmation._id" @click="editAffirmation(affirmation)">
            {{ affirmation.text }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import DataEditor   from './components/DataEditor.vue';
import LandingPage  from './components/LandingPage.vue';
import BinaryEditor from './components/BinaryEditor.vue'; // make sure to import this

export default {
  name: 'App',
  components: {
    DataEditor,
    LandingPage,
    BinaryEditor
  },
  data() {
    return {
      messages:           [],   // to fetch these from server too
      currentRecord:      null,
      currentAffirmation: null, // the current affirmation being edited
      currentView:        'landing'
    };
  },
  mounted() {
    fetch('http://localhost:3001/all_messages')
      .then(res => res.json())
      .then(data => {
        this.messages = data;
      });
  },
  methods: {
    setCurrentView(view) {
      this.currentView = view;
    },
    editRecord(record) {
      this.currentRecord = record;
    },
    editAffirmation(affirmation) { // to edit a specific affirmation
      this.currentAffirmation = affirmation;
    },
    onSaved() {
      this.currentRecord = null;
      this.currentAffirmation = null;
    }
  }
}
</script>
